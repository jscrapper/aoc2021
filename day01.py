from aoc2021 import Day

class Day01(Day):
    def parse_input(self):
        return [int(x) for x in self.raw_puzzle_input]

    def a(self):
        count = -1
        last = 0
        for line in self.puzzle_input:
            if line > last:
                count += 1
            last = line
        return count

    def b(self):
        count = -1
        last = 0
        for i in range(0,len(self.puzzle_input)-2):
            sum=self.puzzle_input[i]+self.puzzle_input[i+1]+self.puzzle_input[i+2]
            if sum > last:
                count += 1
            last = sum
        return count

    def test(self):
        self.puzzle_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        return self.b()

if __name__ == "__main__":
    d=Day01()
    print(d.b())