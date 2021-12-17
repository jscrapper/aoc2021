from aoc2021 import Day
import math
from functools import reduce
from typing import DefaultDict
class Day17(Day):
    def get_input(self):
        return "target area: x=60..94, y=-171..-136"

    def get_test_input(self):
        return "target area: x=20..30, y=-10..-5"

    def parse_input(self):
        result=[]
        for rng in self.raw_puzzle_input.split(": ")[1].split(", "):
            intrng = [int(a) for a in rng.split("=")[1].split("..")]
            result.append( [int(a) for a in rng.split("=")[1].split("..")] )
        self.goal = result
        return result

    def shoot(self, vx, vy):
        pos = [0,0]
        steps = 0
        vel = [vx,vy]
        result = None
        hit=False
        maxy=-9999999
        while pos[0] < self.goal[0][1] and pos[1] > self.goal[1][0]: # not further than our window
            steps += 1
            pos[0] += vel[0]    # update posx
            pos[1] += vel[1]    # update posy
            maxy=max(maxy, pos[1])
            if vel[0] > 0:      # drag vel x toward 0
                vel[0] -= 1
            vel[1] -= 1         # gravity
            if self.goal[0][0] <= pos[0] <= self.goal[0][1] and self.goal[1][0] <= pos[1] <= self.goal[1][1]: # in target window
                result=pos
                hit=True
                break

        return hit, result, maxy

    def findx(self):
        def getallx(x):
            results=[]
            pos=0
            while x >= 0:
                results.append(pos)
                pos += x
                x -= 1
            return results

        hits={}
        for i in range(int(math.sqrt(self.goal[0][0])),self.goal[0][1]+1):
            results=list(filter(lambda x: self.goal[0][0] <= x <= self.goal[0][1], getallx(i)))
            if len(results)>0:
                hits[i] = results

        return hits

    def findhits(self):
        hits=DefaultDict(int)
        for x, step in self.findx().items():
            # does y hit? 
            for y in range(self.goal[1][0],abs(self.goal[1][0])):
                hit, pos, maxy = self.shoot(x,y)
                if hit:
                    hits[(x,y)]=maxy
        return hits

    def a(self):
        # result = self.shoot(7,2)
        # print(result)
        # result = self.shoot(6,3)
        # print(result)
        # result = self.shoot(9,0)
        # print(result)
        # result = self.shoot(17,-4)
        # print(result)
        hits = self.findhits()

        return sorted(hits.values(), reverse=True)[0]

    def b(self):
        hits = self.findhits()
        return len(hits)

if __name__ == "__main__":
    Day17(False).run()