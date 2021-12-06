from aoc2021 import Day
import numpy as np
import numpy.ma as ma

class Board():
    def __init__(self, input):
        self.board = ma.array(input, dtype=np.int8, order='F')
    
    def call(self, number):
        for iy,y in enumerate(self.board):
            for ix,x in enumerate(y):
                if x == number:
                    self.board[iy,ix]=ma.masked
        return self.validate()
    
    def validate(self):
        if 5 in np.sum(ma.getmaskarray(self.board), axis=0):
            return True
        if 5 in np.sum(ma.getmaskarray(self.board), axis=1):
            return True
        return False
    
    def sum(self):
        return ma.sum(self.board)

class Day04(Day):
    def parse_input(self):
        self.draw = [int(x) for x in self.raw_puzzle_input[0].split(",")]
        self.boards = []
        for i in range(2, len(self.raw_puzzle_input), 6):
            self.boards.append(Board([self.raw_puzzle_input[i+j].split() for j in range(5)]))
        return

    def a(self):
        for x in self.draw:
            for b in self.boards:
                if b.call(x):
                    return b.sum() * x

    def b(self):
        rm = []
        for x in self.draw:
            for ib, b in enumerate(self.boards):
                if b.call(x):
                    if len(self.boards) == 1:
                        return b.sum() * x
                    else:
                        rm.append(ib)
            for r in sorted(rm, reverse=True):
                self.boards.pop(r)
            rm=[]

    def test(self):
        self.raw_puzzle_input = ["7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
        "",
        "22 13 17 11  0",
        " 8  2 23  4 24",
        "21  9 14 16  7",
        " 6 10  3 18  5",
        " 1 12 20 15 19",
        "",
        " 3 15  0  2 22",
        " 9 18 13 17  5",
        "19  8  7 25 23",
        "20 11 10 24  4",
        "14 21 16 12  6",
        "",
        "14 21 17 24  4",
        "10 16 15  9 19",
        "18  8 23 26 20",
        "22 11 13  6  5",
        " 2  0 12  3  7"]
        self.parse_input()
        self.b()

if __name__ == "__main__":
    Day04().run()