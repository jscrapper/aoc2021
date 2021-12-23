import os
from contextlib import contextmanager
from time import perf_counter
import numpy as np
from queue import PriorityQueue, Queue

class Day(object):
    def __init__(self, test=False, profile=False):
        self.raw_puzzle_input = self.get_test_input() if test else self.get_input()
        self.puzzle_input = self.parse_input()
        self.profile = profile

    def get_input(self):
        """ Gets the puzzle input from a text file in the same folder, with a name matching the classname, and the extension '.txt' """
        filename = os.path.join(os.path.dirname(__file__), self.__class__.__name__+".txt")
        with open(filename, 'r') as f:
            raw_puzzle_input = f.read().splitlines()
        return raw_puzzle_input

    def get_test_input(self):
        return []

    def parse_input(self):
        return self.raw_puzzle_input

    def a(self):
        raise NotImplementedError

    def b(self):
        raise NotImplementedError

    def run(self, force_reparse=False):
        with timer() as t:
            a_result = self.a()
        
        msg = f"A: {a_result}"
        if self.profile:
            msg += f" Completed in {t.time:.4f}s."
        print(msg)

        if force_reparse:
            self.puzzle_input = self.parse_input()

        with timer() as t:
            b_result = self.b()
        
        msg = f"B: {b_result}"
        if self.profile:
            msg += f" Completed in {t.time:.4f}s."
        print(msg)

class Graph():
    def __init__(self, grid, allow_diagonal:bool=False, t:type=int):
        self.grid = grid
        self.allow_diagonal = allow_diagonal

    def neighbors(self, iy, ix):
        offsets= [ (iy-1,ix), (iy,ix+1), (iy,ix-1), (iy+1,ix) ]
        if self.allow_diagonal:
            offsets+=[(iy-1,ix-1),(iy-1,ix+1),(iy+1,ix-1),(iy+1,ix+1)]
        for niy, nix in offsets:
            if 0 <= niy < self.grid.shape[0] and 0 <= nix < self.grid.shape[1]:
                yield (niy, nix)
            
    def _reconstruct_path(self, came_from, start, goal, include_start:bool=False, reverse:bool=False):
        current = goal
        path=[]
        while current != start:
            path.append(current)
            current = came_from[current]
        if include_start:
            path.append(start)
        if reverse:
            path.reverse()
        return path

    def _dijkstra(self, start, goal):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = dict()
        cost_so_far = dict()
        came_from[start]=None
        cost_so_far[start]=0

        while not frontier.empty():
            current = frontier.get()
            if current == goal:
                break

            for next in self.neighbors(*current):
                new_cost = cost_so_far[current] + self.grid[next]
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    frontier.put(next, new_cost)    # new cost is the priority here for the next element. 
                    came_from[next] = current
        
        return came_from, cost_so_far

    def get_path_dijkstra(self, start, goal):
        came_from, cost_so_far = self._dijkstra(start, goal)
        return self._reconstruct_path(came_from, start, goal, reverse=True)

    @property
    def shape(self):
        return self.grid.shape

    

class timer:
    def __enter__(self):
        self.time = perf_counter()
        return self
    
    def __exit__(self, type, value, traceback):
        self.time = perf_counter() - self.time
