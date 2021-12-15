from aoc2021 import Day, Graph
import numpy as np

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
        pass

if __name__ == "__main__":
    Day15(False).run()