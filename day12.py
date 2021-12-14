from aoc2021 import Day
from collections import defaultdict
from queue import Queue

class Day12(Day):

    def get_test_input(self):
        return ["start-A",
                "start-b",
                "A-c",
                "A-b",
                "b-d",
                "A-end",
                "b-end"]
    
    def parse_input(self):
        neighbors = defaultdict(list)
        for x in self.raw_puzzle_input:
            a,b = x.split("-")
            neighbors[a].append(b)
            neighbors[b].append(a)
        return neighbors

    def dfs(self, current, start, end, visited, twice):
        if current == end: return 1
        count=0
        for neighbor in self.puzzle_input[current]:
            if not neighbor.islower() or neighbor not in visited:
                count += self.dfs(neighbor, start, end, visited | {neighbor}, twice)
            elif twice and neighbor not in {start, end}:
                count += self.dfs(neighbor, start, end, visited | {neighbor}, False)
        return count 

    def a(self):
        return self.dfs("start", "start", "end", {"start"}, False)

    def b(self):
        return self.dfs("start", "start", "end", {"start"}, True)

if __name__ == "__main__": 
    Day12().run()