from aoc2021 import Day
import numpy as np
from itertools import accumulate

class Day07(Day):
    def parse_input(self):
        return [int(x) for x in self.raw_puzzle_input[0].split(",")]

    def get_test_input(self):
        return ["16,1,2,0,4,2,7,1,2,14"]

    def a(self):
        positions = np.array(self.puzzle_input, dtype=np.uint32)
        min_fuel = 9999999
        for i in range(positions.min(), positions.max()):
            min_fuel = min(np.sum([abs(pos - i) for pos in positions]), min_fuel)
        return min_fuel

    def lookup(self, pos):
        if not hasattr(self, 'cache'):
            self.cache = {}
        if pos not in self.cache:
            self.cache[pos] = sum(accumulate(np.ones(abs(pos), dtype=np.uint32)))
        return self.cache[pos]

    def b(self):
        positions = np.array(self.puzzle_input, dtype=np.uint32)
        min_fuel = 9999999999999999
        for i in range(positions.min(), positions.max()):
            min_fuel = min(sum([ self.lookup(pos - i) for pos in positions]), min_fuel)
        return min_fuel

if __name__ == "__main__": 
    Day07(profile=True).run()