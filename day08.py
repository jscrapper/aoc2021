from typing import Counter
from aoc2021 import Day
from typing import Counter

class Display():
    """
      0:      1:      2:      3:      4:
     aaaa    ....    aaaa    aaaa    ....
    b    c  .    c  .    c  .    c  b    c
    b    c  .    c  .    c  .    c  b    c
     ....    ....    dddd    dddd    dddd
    e    f  .    f  e    .  .    f  .    f
    e    f  .    f  e    .  .    f  .    f
     gggg    ....    gggg    gggg    ....

      5:      6:      7:      8:      9:
     aaaa    aaaa    aaaa    aaaa    aaaa
    b    .  b    .  .    c  b    c  b    c
    b    .  b    .  .    c  b    c  b    c
     dddd    dddd    ....    dddd    dddd
    .    f  e    f  .    f  e    f  .    f
    .    f  e    f  .    f  e    f  .    f
     gggg    gggg    ....    gggg    gggg
    """

    def __init__(self, signal_wires):
        """ expecting a list of 10 strings which define the signal wires for each segment of a seven segment display"""
        self.signal_wires = signal_wires

        # the display will be the digit as the key, and a set of characters that represent each segment. 
        # for this case we don't care where they are exactly, since we're just deriving them via subsets of each other. 
        self.display = {}
        # These are unique by count.
        self.display[1]=set(list(filter(lambda x: len(x)==2, signal_wires))[0])
        self.display[4]=set(list(filter(lambda x: len(x)==4, signal_wires))[0])
        self.display[7]=set(list(filter(lambda x: len(x)==3, signal_wires))[0])
        self.display[8]=set(list(filter(lambda x: len(x)==7, signal_wires))[0])

        # these are 6,9,0
        six_count = [set(x) for x in list(filter(lambda x: len(x)==6, signal_wires))]
        # find 9 - 4 is a subset of 9 but not 0 or 6.
        for x in six_count:
            if self.display[4].issubset(x):
                self.display[9]=x
                six_count.remove(x)
                break
        # find 0 - 7 is a subset of 0 but not 6.
        for x in six_count: 
            if self.display[7].issubset(x):
                self.display[0]=x
                six_count.remove(x)
                break
        # whats left is 6.
        self.display[6] = six_count.pop()

        # these are 2,3,5 
        five_count = [set(x) for x in list(filter(lambda x: len(x)==5, signal_wires))]
        # find 3 - 7 is a subset of 3 but not 2 or 5. 
        for x in five_count:
            if self.display[7].issubset(x):
                self.display[3]=x
                five_count.remove(x)
                break
        # find 5: it's a subset of 9.
        for x in five_count:
            if x.issubset(self.display[9]):
                self.display[5]=x
                five_count.remove(x)
                break
        # 2 remains
        self.display[2] = five_count.pop()
    
    def get_digit(self, segments):
        """given a string of segments that are lit up, return the digit they represent."""
        s=set(segments)
        for digit, signature in self.display.items():
            if signature == s:
                return digit


class Day08(Day):
    def parse_input(self):
        results = [0]*len(self.raw_puzzle_input)
        for i, line in enumerate(self.raw_puzzle_input):
            digits, output = line.split(" | ")
            results[i]=(digits.split(), output.split())
        return results

    def get_test_input(self):
        # return ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
        return ["be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
                "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
                "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
                "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
                "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
                "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
                "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
                "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
                "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
                "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"]

    def a(self):
        # unique segment counts for 1, 4, 7, 8
        unique_signals = [2, 4, 3, 7]
        count = 0
        for signal in self.puzzle_input:
            c=Counter([len(x) for x in signal[1]])
            count += sum([c[s] for s in unique_signals])
        return count

    def b(self):
        results = []
        for signal, digits in self.puzzle_input:
            display = Display(signal)
            value=""
            for digit in digits:
                value += str(display.get_digit(digit))
            results.append(int(value))
        return sum(results)

if __name__ == "__main__": 
    Day08().run()