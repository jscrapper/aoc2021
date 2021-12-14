from aoc2021 import Day
import numpy as np
from copy import deepcopy
from typing import Counter

class Day13(Day):
    def get_test_input(self):
        return ["6,10",
                "0,14",
                "9,10",
                "0,3",
                "10,4",
                "4,11",
                "6,0",
                "6,12",
                "4,1",
                "0,13",
                "10,12",
                "3,4",
                "3,0",
                "8,4",
                "1,10",
                "2,14",
                "8,10",
                "9,0",
                "",
                "fold along y=7",
                "fold along x=5"]
                
    def parse_input(self):
        instructions=[]
        coords=[]
        for line in self.raw_puzzle_input:
            if len(line) > 0:
                if line[0] == "f":  # instruction
                    axis,val = line.split("=")
                    axis = 0 if axis[-1:] == "y" else 1
                    val = int(val)
                    instructions.append((axis,val))
                else:               # coord
                    x,y = line.split(",")
                    coords.append((int(y),int(x)))
        grid = np.zeros(np.amax(coords, 0)+1, dtype=np.uint)
        for coord in coords:
            grid[coord] = 1
        return grid, instructions, coords

    def fold(self, grid, instructions):
        for axis, i in instructions:
            a,nope,b = np.split(grid,[i, i+1], axis)
            bflip = np.flip(b, axis)
            grid = np.add(bflip, a)
        return grid

    def print(self, grid):
        output=""
        for y in grid:
            for x in y:
                output += "." if x==0 else "#"
            output += "\n"
        print(output)

    def a(self):
        basegrid, instructions, coords = self.puzzle_input
        grid = deepcopy(basegrid)
        result = self.fold(grid, [instructions[0]])
        return np.count_nonzero(result)

    def b(self):
        basegrid, instructions, coords = self.puzzle_input
        grid = deepcopy(basegrid)
        result = self.fold(grid, instructions)
        self.print(result)
        return

if __name__ == "__main__":
    Day13().run()