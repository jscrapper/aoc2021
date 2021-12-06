from aoc2021 import Day
import numpy as np
from typing import Counter

class Day05(Day):

    def parse_input(self):
        result = []
        for line in self.raw_puzzle_input:
            a,b = line.split(" -> ")
            x1,y1 = map(int,a.split(","))
            x2,y2 = map(int,b.split(","))
            result.append(((x1,y1), (x2,y2)))
        self.grid = np.zeros((999,999), dtype=np.int8)
        return result

    def a(self):
        for vent in self.puzzle_input:
            if vent[0][0] == vent[1][0] or vent[0][1] == vent[1][1]:
                sorted_y = sorted([vent[0][1], vent[1][1]])
                sorted_x = sorted([vent[0][0], vent[1][0]])

                for iy in range(sorted_y[0], sorted_y[1]+1):
                    for ix in range(sorted_x[0], sorted_x[1]+1):
                        self.grid[iy,ix]+=1

        count = np.count_nonzero(self.grid > 1)
        return count


    def b(self):
        for vent in self.puzzle_input:
            if vent[0][0] == vent[1][0] or vent[0][1] == vent[1][1]:
                sorted_y = sorted([vent[0][1], vent[1][1]])
                sorted_x = sorted([vent[0][0], vent[1][0]])

                for iy in range(sorted_y[0], sorted_y[1]+1):
                    for ix in range(sorted_x[0], sorted_x[1]+1):
                        self.grid[iy,ix]+=1

            diag = vent[0][0]-vent[1][0] == vent[0][1] - vent[1][1]
            if diag:
                flipy = vent[0][1] > vent[1][1]
                flipx = vent[0][0] > vent[1][0]
                step = -1 if flipy else 1
                for i,j in enumerate(range(vent[0][1], vent[1][1] + step)):
                    x=vent[0][0]-i if flipx else vent[0][0]+i
                    self.grid[j, x] += 1

        count = np.count_nonzero(self.grid > 1)
        return count

    def test(self):
        self.raw_puzzle_input = ["0,9 -> 5,9",
            "8,0 -> 0,8",
            "9,4 -> 3,4",
            "2,2 -> 2,1",
            "7,0 -> 7,4",
            "6,4 -> 2,0",
            "0,9 -> 2,9",
            "3,4 -> 1,4",
            "0,0 -> 8,8",
            "5,5 -> 8,2"]
        self.puzzle_input = self.parse_input()
        self.b()

if __name__ == "__main__":
    Day05().test()