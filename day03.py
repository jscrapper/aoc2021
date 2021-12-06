from typing import Counter
from aoc2021 import Day

class Day03(Day):
    def parse_input(self):
        return [line for line in self.raw_puzzle_input]

    @property
    def num_bits(self):
        return len(self.puzzle_input[0])

    def a(self):
        gamma=""
        for i in range(self.num_bits):
            c=Counter([x[i] for x in self.puzzle_input])
            gamma+=c.most_common(1)[0][0]
        igamma=int(gamma,2)
        ones = int("".join(["1"]*self.num_bits),2)
        iepsilon=igamma ^ ones
        return igamma * iepsilon

    def b(self):
        o2=self.puzzle_input
        for i in range(self.num_bits):
            count_o2=Counter([x[i]for x in o2]).most_common()
            if len(count_o2) <= 1: break
            if count_o2[0][1] == count_o2[1][1]:
                o2=list(filter(lambda x: x[i] == "1", o2))      # 1 will be last when equal
            else:
                o2=list(filter(lambda x: x[i] == count_o2[0][0], o2))       # pick most common
        io2=int(o2[0],2)

        co2=self.puzzle_input
        for i in range(self.num_bits):
            count_co2=Counter([x[i]for x in co2]).most_common()
            if len(count_co2) <= 1: break
            if count_co2[0][1] == count_co2[1][1]:
                co2=list(filter(lambda x: x[i] == "0", co2))    # use 0, the first one, when equal. 
            else:
                co2=list(filter(lambda x: x[i] == count_co2[-1][0], co2))   # pick least common 
        ico2=int(co2[0],2)

        return io2*ico2

    def test(self):
        self.puzzle_input = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]
        return self.b()

if __name__ == "__main__":
    Day03().run()