from aoc2021 import Day, Graph
import numpy as np
from scipy.ndimage import generic_filter

class Day20(Day):
    def get_test_input(self):
        return ["..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#",
                "",
                "#..#.",
                "#....",
                "##..#",
                "..#..",
                "..###"]

    def parse_input(self):
        self.enhancement = list(map(lambda x: int(0) if x=="." else 1, self.raw_puzzle_input[0]))
        h=len(self.raw_puzzle_input)-2
        w=len(self.raw_puzzle_input[2])
        self.image = np.zeros(shape=(h,w), dtype=np.int32)
        for yi, y in enumerate(self.raw_puzzle_input[2:]):
            for xi, x in enumerate(y):
                self.image[yi,xi] = 0 if x == "." else 1
        # self.image = np.array(map(lambda x: int(0 if x == "." else 1),self.raw_puzzle_input[2:]))
        # self.image = np.pad(self.image,1)
        return

    def enhance(self, im, pad_val=1):
        def _filter(f):
            """ image generic filter function, make a binary string from our 3x3 window, 
            then look that up in the image enhancement algorithm"""
            s=""
            for v in f:
                s+=str(int(v))
            d=int(s,2)
            return self.enhancement[d]

        imout=np.pad(im, 2, constant_values=pad_val)
        filtered = generic_filter(imout, _filter, size=(3,3), mode='constant', cval=pad_val)

        return filtered

    def a(self):
        im=self.image
        for i in range(2):
            pad = i%2 if self.image[0,0] == 1 else 1
            im = self.enhance(im, pad_val=pad)
        
        return np.sum(im)

    def b(self):
        im=self.image
        for i in range(50):
            pad = i%2 if self.image[0,0] == 1 else 1
            im = self.enhance(im, pad_val=pad)
        
        return np.sum(im)

if __name__ == "__main__":
    Day20().run()