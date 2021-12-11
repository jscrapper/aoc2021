from aoc2021 import Day
import numpy as np
from queue import Queue
from copy import deepcopy

class Day11(Day):
    def get_test_input(self):
        return ["5483143223",
                "2745854711",
                "5264556173",
                "6141336146",
                "6357385478",
                "4167524645",
                "2176841721",
                "6882881134",
                "4846848554",
                "5283751526"]

    def parse_input(self):
        for i in range(len(self.raw_puzzle_input)):
            self.raw_puzzle_input[i] = [int(x) for x in self.raw_puzzle_input[i]]
        return np.array(self.raw_puzzle_input, dtype=np.uint8) 
    
    def neighbors(self, iy, ix):
        n= [(iy-1,ix-1), (iy-1,ix), (iy-1,ix+1), (iy,ix+1), (iy,ix-1), (iy+1,ix-1), (iy+1,ix), (iy+1,ix+1)]
        for niy, nix in n:
            if 0 <= niy < len(self.grid) and 0 <= nix < len(self.grid[0]):
                yield (niy, nix)
    
    def print(self):
        s=""
        for y in self.grid:
            s+="".join(map(str, y))+"\n"
        print(s)

    def step(self):
        frontier = Queue()
        flashed = set()
        for iy, y in enumerate(self.grid):
            for ix, x in enumerate(y):
                self.grid[iy,ix] += 1
                if self.grid[iy,ix] > 9:    #flash
                    frontier.put((iy,ix))
                    flashed.add((iy,ix))

        # feedback flashing
        while not frontier.empty():
            current = frontier.get()
            for n in self.neighbors(*current):
                self.grid[n] += 1
                if self.grid[n] > 9 and n not in flashed:
                    frontier.put(n)
                    flashed.add(n)
        
        # reset flashed to 0
        self.flashcount+=len(flashed)
        for x in flashed:
            self.grid[x] = 0

    def a(self):
        self.grid = deepcopy(self.puzzle_input)

        self.flashcount = 0
        # print(f"step {0}, flashcount {self.flashcount}:")
        # self.print()
        for i in range(1,101):
            self.step()
            # print(f"step {i}, flashcount {self.flashcount}:")
            # self.print()
        return self.flashcount

    def b(self):
        self.grid = deepcopy(self.puzzle_input)

        step=0
        while np.sum(self.grid) > 0:
            step += 1
            self.step()
        return step

if __name__ == "__main__":
    Day11().run()