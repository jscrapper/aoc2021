from aoc2021 import Day, Graph
import numpy as np
from copy import deepcopy

class Day15(Day):
    def get_test_input(self):
        return ["1163751742",
                "1381373672",
                "2136511328",
                "3694931569",
                "7463417111",
                "1319128137",
                "1359912421",
                "3125421639",
                "1293138521",
                "2311944581"]
    
    def parse_input(self):
        # cast to ints
        for i in range(len(self.raw_puzzle_input)):
            self.raw_puzzle_input[i] = [int(x) for x in self.raw_puzzle_input[i]]
        input = np.array(self.raw_puzzle_input)
        return Graph(input) # expects a numpy array.

    def neighbors(self, iy, ix):
        for niy, nix in [(iy-1,ix), (iy,ix-1), (iy+1,ix), (iy,ix+1)]:
            if 0 <= niy < len(self.puzzle_input) and 0 <= nix < len(self.puzzle_input[0]):
                yield (niy, nix)

    def a(self):
        goal = tuple([x-1 for x in self.puzzle_input.shape])
        p=self.puzzle_input.get_path_dijkstra((0,0), goal)
        cost = [self.puzzle_input.grid[x] for x in p]
        s = sum(cost)
        return s

    def b(self):
        num_tiles = 5
        base_y, base_x=self.puzzle_input.shape
        graph = np.tile(self.puzzle_input.grid, (num_tiles, num_tiles))        
        for y in range(num_tiles):
            for x in range(num_tiles):
                graph[y*base_y:y*base_y+base_y, x*base_x:x*base_x+base_x]+=x+y
        # wrap to 1
        for idx, val in np.ndenumerate(graph):
            if val > 9:
                graph[idx]-=9
        self.puzzle_input.grid = graph
        goal = tuple([x-1 for x in self.puzzle_input.shape])
        p=self.puzzle_input.get_path_dijkstra((0,0), goal)
        cost = [self.puzzle_input.grid[x] for x in p]
        s = sum(cost)

        ma = np.ma.array(self.puzzle_input.grid, dtype=np.uint8)
        for loc in p:
            ma[loc]=np.ma.masked

        return s

if __name__ == "__main__":
    Day15(False, True).run()