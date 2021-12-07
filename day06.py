from aoc2021 import Day
import numpy as np
from typing import Counter

class Day06(Day):
    def parse_input(self):
        return [int(x) for x in self.raw_puzzle_input[0].split(",")]

    def get_test_input(self):
        return ["3,4,3,1,2"]

    def sim_brute(self, days):
        """brute force simming exponential growth of fishes over N days
        This solution is unwieldy as the size grows, for the 256 count 
        event the test input takes an unreasonable amount of time."""
        fishes = self.puzzle_input
        # brute force
        for d in range(days):
            create_count = 0
            for i, fish in enumerate(fishes):
                fishes[i] = fish - 1 
                if fishes[i] < 0:
                    fishes[i] = 6
                    create_count += 1
            # add new fish
            new_fish = [8]*create_count
            fishes += new_fish
            create_count = 0
        return len(fishes)

    def sim(self, days):
        fishes = np.zeros((9),dtype=np.uint64)
        counter = Counter(self.puzzle_input)
        for x in counter:
            fishes[x]=counter[x]
        
        for d in range(days):
            fishes = np.roll(fishes, -1)
            fishes[6] = fishes[6] + fishes[8]
        return fishes.sum()

    def a(self):
        return self.sim(80)

    def b(self):
        return self.sim(256)

if __name__ == "__main__": 
    Day06().run()