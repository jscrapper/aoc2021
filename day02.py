from aoc2021 import Day
import operator

class Day02(Day):
    
    def parse_input(self):
        return [x.split() for x in self.raw_puzzle_input]
    
    def a(self):
        pos=0
        depth = 0
        for x in self.puzzle_input:
            dir = x[0]
            dist = int(x[1])
            if dir == "forward":
                pos += int(x[1])
            elif dir == "up":
                depth -= dist
            elif dir == "down":
                depth += dist

        result = pos * depth
        print(f"A: hpos {pos}, depth {depth}, result: {result}")
        return result

    def b(self):
        pos = 0
        depth = 0
        aim = 0
        for x in self.puzzle_input:
            dir = x[0]
            dist = int(x[1])
            if dir == "forward":
                pos += dist
                depth += aim * dist
            if dir == "up":
                aim -= dist
            if dir == "down":
                aim += dist
        
        result = pos * depth
        print(f"B: hpos {pos}, depth {depth}, result: {result}")
        return result


if __name__ == "__main__":
    Day02().run()