import os
from contextlib import contextmanager
from time import perf_counter

class Day(object):
    def __init__(self, test=False, profile=False):
        self.raw_puzzle_input = self.get_test_input() if test else self.get_input()
        self.puzzle_input = self.parse_input()
        self.profile = profile

    def get_input(self):
        """ Gets the puzzle input from a text file in the same folder, with a name matching the classname, and the extension '.txt' """
        filename = os.path.join(os.path.dirname(__file__), self.__class__.__name__+".txt")
        with open(filename, 'r') as f:
            raw_puzzle_input = f.read().splitlines()
        return raw_puzzle_input

    def get_test_input(self):
        return []

    def parse_input(self):
        return self.raw_puzzle_input

    def a(self):
        raise NotImplementedError

    def b(self):
        raise NotImplementedError

    def run(self):
        with timer() as t:
            a_result = self.a()
        
        msg = f"A: {a_result}"
        if self.profile:
            msg += f" Completed in {t.time:.4f}s."
        print(msg)

        with timer() as t:
            b_result = self.b()
        
        msg = f"A: {b_result}"
        if self.profile:
            msg += f" Completed in {t.time:.4f}s."
        print(msg)

class timer:
    def __enter__(self):
        self.time = perf_counter()
        return self
    
    def __exit__(self, type, value, traceback):
        self.time = perf_counter() - self.time
