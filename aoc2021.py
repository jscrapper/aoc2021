import os

class Day(object):
    def __init__(self):
        self.raw_puzzle_input = self.get_input()
        self.puzzle_input = self.parse_input()

    def get_input(self):
        """ Gets the puzzle input from a text file in the same folder, with a name matching the classname, and the extension '.txt' """
        filename = os.path.join(os.path.dirname(__file__), self.__class__.__name__+".txt")
        with open(filename, 'r') as f:
            raw_puzzle_input = f.read().splitlines()
        return raw_puzzle_input

    def parse_input(self):
        return self.raw_puzzle_input

    def a(self):
        raise NotImplementedError

    def b(self):
        raise NotImplementedError

    def run(self):
        print(f"A: {self.a()}")
        print(f"B: {self.b()}")