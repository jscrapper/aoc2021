from aoc2021 import Day
from copy import deepcopy
from typing import Counter
from collections import defaultdict
from cProfile import Profile

class Day14(Day):
    def get_test_input(self):
        return ["NNCB",
                "",
                "CH -> B",
                "HH -> N",
                "CB -> H",
                "NH -> C",
                "HB -> C",
                "HC -> B",
                "HN -> C",
                "NN -> C",
                "BH -> H",
                "NC -> B",
                "NB -> B",
                "BN -> B",
                "BB -> N",
                "BC -> B",
                "CC -> N",
                "CN -> C"]

    def parse_input(self):
        self.template = self.raw_puzzle_input[0] # strings are immutable so let's treat the polymer as a list.
        self.rules = {}
        for x in self.raw_puzzle_input[2:]:
            pair, insert = x.split(" -> ")
            self.rules[pair]=insert

    def chain_brute(self, polymer, steps):
        polymer = list(polymer)
        for step in range(steps):
            for i in range(len(polymer)-2, -1, -1):
                pair = "".join(polymer[i:i+2])
                if pair in self.rules:
                    polymer.insert(i+1, self.rules[pair])
        return Counter(polymer)

    def chain(self, polymer, steps):
        counts = Counter(polymer)
        pairs = Counter()
        for i in range(len(polymer)-2, -1, -1):
            pairs[polymer[i:i+2]]+=1

        for step in range(steps):
            step_pairs = Counter()
            for pair in pairs:
                if pair not in self.rules:
                    continue
                ins = self.rules[pair]
                p0 = pair[0] + ins
                p1= ins + pair[1]

                increment = pairs[pair]
                step_pairs[p0] += increment
                step_pairs[p1] += increment
                counts[ins] += increment

            pairs = step_pairs
        return counts

    def a(self):
        c = self.chain(self.template, 10).most_common()
        return c[0][1] - c[-1][1]

    def b(self):
        c = self.chain(self.template, 40).most_common()
        return c[0][1] - c[-1][1]

if __name__ == "__main__":
    Day14().run()