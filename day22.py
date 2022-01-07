from aoc2021 import Day
import numpy as np
from typing import Counter
from itertools import product

class Day22(Day):
    def get_test_input(self):
        return ["on x=-20..26,y=-36..17,z=-47..7",
                "on x=-20..33,y=-21..23,z=-26..28",
                "on x=-22..28,y=-29..23,z=-38..16",
                "on x=-46..7,y=-6..46,z=-50..-1",
                "on x=-49..1,y=-3..46,z=-24..28",
                "on x=2..47,y=-22..22,z=-23..27",
                "on x=-27..23,y=-28..26,z=-21..29",
                "on x=-39..5,y=-6..47,z=-3..44",
                "on x=-30..21,y=-8..43,z=-13..34",
                "on x=-22..26,y=-27..20,z=-29..19",
                "off x=-48..-32,y=26..41,z=-47..-37",
                "on x=-12..35,y=6..50,z=-50..-2",
                "off x=-48..-32,y=-32..-16,z=-15..-5",
                "on x=-18..26,y=-33..15,z=-7..46",
                "off x=-40..-22,y=-38..-28,z=23..41",
                "on x=-16..35,y=-41..10,z=-47..6",
                "off x=-32..-23,y=11..30,z=-14..3",
                "on x=-49..-5,y=-3..45,z=-29..18",
                "off x=18..30,y=-20..-8,z=-3..13",
                "on x=-41..9,y=-7..43,z=-33..15",
                "on x=-54112..-39298,y=-85059..-49293,z=-27449..7877",
                "on x=967..23432,y=45373..81175,z=27513..53682"]

    def parse_input(self):
        instructions = []
        self.min = 0
        self.max = 0
        for line in self.raw_puzzle_input:
            state=0
            header=4
            if "on" in line:
                state=1
                header=3
            instruction = []
            cmd=[]
            for comp in line[header:].split(","):
                irng = tuple(map(int, comp[2:].split("..")))
                self.min = min(min(irng),self.min)
                self.max = max(max(irng),self.max)
                cmd.append(irng)
            instructions.append((cmd, state))
        return instructions

    def a(self):
        """ np array - straightforward approach """
        self.offset = np.array((-50,-50,-50), dtype=np.int32)
        self.grid = np.zeros((101,101,101), dtype=np.bool8)

        for step in self.puzzle_input:
            cmd,state=step
            icmd = np.add(cmd, 50)   # offset to grid coords
            if np.min(icmd) >= 0 and np.max(icmd) <= 100:
                self.grid[icmd[0][0]:icmd[0][1]+1, icmd[1][0]:icmd[1][1]+1, icmd[2][0]:icmd[2][1]+1] = state
        return np.sum(self.grid)

    def b(self):
        """ too much memory for a full grid, or even a set of coordinates 
        @TODO: look into set theory https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle
         """ 
        pass


if __name__ == "__main__":
    Day22(True).run()
