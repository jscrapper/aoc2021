from aoc2021 import Day
import numpy as np
from queue import Queue

class Day09(Day):

    def get_test_input(self):
        return ["2199943210",
                "3987894921",
                "9856789892",
                "8767896789",
                "9899965678"]
    
    def parse_input(self):
        for i in range(len(self.raw_puzzle_input)):
            self.raw_puzzle_input[i] = [int(x) for x in self.raw_puzzle_input[i]]
        return np.array(self.raw_puzzle_input, dtype=np.uint8)

    def a(self):
        """ find a low point, locations that are less than all neighbors. 
        calculate the risk of low points as 1+height, return the summed risk."""
        low_values = [self.puzzle_input[y,x] for y,x in self.low_points()]
        return sum(low_values)+len(low_values)

    def neighbors(self, iy, ix):
        for niy, nix in [(iy-1,ix), (iy,ix-1), (iy+1,ix), (iy,ix+1)]:
            if 0 <= niy < len(self.puzzle_input) and 0 <= nix < len(self.puzzle_input[0]):
                yield (niy, nix)
            
    def low_points(self):
        for iy, y in enumerate(self.puzzle_input):
            for ix,x in enumerate(y):
                neighbors_larger = []
                for niy, nix in self.neighbors(iy, ix):
                    neighbors_larger.append(self.puzzle_input[niy,nix] > x)
                if all(neighbors_larger):
                    yield (iy,ix)

    def b(self):
        basins = []
        for pt in self.low_points():
            frontier = Queue()
            frontier.put(pt)
            visited = set()
            visited.add(pt)
            while not frontier.empty():
                current = frontier.get()
                for next in self.neighbors(*current):
                    if self.puzzle_input[next] < 9 and next not in visited:
                        frontier.put(next)
                        visited.add(next)
            basins.append(len(visited))
        return np.prod(sorted(basins)[-3:])

if __name__ == "__main__": 
    Day09().run()