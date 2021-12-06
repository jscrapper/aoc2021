from aoc2021 import Day
import numpy as np
from typing import Counter

class Day05(Day):

    def parse_input(self):
        result = []
        max_x=0
        max_y=0
        for line in self.raw_puzzle_input:
            a,b = line.split(" -> ")
            x1,y1 = map(int,a.split(","))
            x2,y2 = map(int,b.split(","))
            max_x = max(max_x, x1, x2)
            max_y = max(max_y, y1, y2)
            result.append(((x1,y1), (x2,y2)))
        self.grid = np.zeros((max_y+1,max_x+1), dtype=np.int8)
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

            diag = abs(vent[0][0]-vent[1][0]) == abs(vent[0][1] - vent[1][1])
            if diag:
                flipy = vent[0][1] > vent[1][1]
                x1=vent[0][0]
                x2=vent[1][0]
                y1=vent[0][1]
                y2=vent[1][1]
                if flipy:
                    x1=vent[1][0]
                    x2=vent[0][0]
                    y1=vent[1][1]
                    y2=vent[0][1]
                
                flipx = x1 > x2
                
                for i,y in enumerate(range(y1,y2+1)):
                    x=x1-i if flipx else x1+i
                    self.grid[y][x] += 1

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
    Day05().b()