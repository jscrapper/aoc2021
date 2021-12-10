from aoc2021 import Day
import numpy as np
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
        risks = []
        for i, y in enumerate(self.puzzle_input):
            for j,x in enumerate(y):
                # test if this value is less than all other neighbors. 
                neighbors_larger = []
                for ny, nx in [(i-1,j), (i,j-1), (i+1,j), (i,j+1)]:
                    if 0 <= ny < len(self.puzzle_input) and 0 <= nx < len(self.puzzle_input[0]):
                        neighbors_larger.append(self.puzzle_input[ny,nx] > x)
                if all(neighbors_larger):
                    risks.append(x+1)
        return sum(risks)

    def b(self):
        pass


if __name__ == "__main__": 
    Day09().run()