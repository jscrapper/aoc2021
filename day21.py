from typing import Counter
from functools import reduce
from itertools import product
from aoc2021 import Day

class DeterministicDice:
    def __init__(self, starting_index):
        self.index=starting_index-1
        self.counter=0
    def roll(self):
        result = 0
        for _ in range(3):
            self.index += 1
            if self.index > 100:
                self.index = 1
            result += self.index
            self.counter += 1
        return result

class Day21(Day):
    def get_input(self):
        return 4,6

    def get_test_input(self):
        return 4,8

    def a(self):
        # change the positions to be 0 indexed for easy modulo. 
        positions=[x - 1 for x in self.puzzle_input]
        scores=[0,0]
        # change dice to be 0 indexed for easy modulo as well. 
        dice = DeterministicDice(1)
        winning_score = 1000
        game_running = True
        while game_running:
            for i in range(2):
                positions[i] = (positions[i] + dice.roll()) % 10
                # remember when incrementing the scores that the positions are one off. 
                scores[i] += positions[i] + 1
                if scores[i] >= winning_score:
                    game_running = False
                    break
        print(f"completed game, positions: {positions}, scores: {scores}, dice: {dice.counter}")
        return sorted(scores)[0] * dice.counter

    def b(self):
        wins=Counter()
        # p0 pos, p0 score, p1 pos, p1 score
        games = Counter()
        # prime initial state
        # remember we're using base index 0 
        games[(self.puzzle_input[0]-1, 0, self.puzzle_input[1]-1, 0)] += 1
        
        winning_score = 21

        # lookup for roll result to universes spawned 
        dice_rolls = Counter(map(lambda w: reduce(lambda x,y:x+y,w), product(range(1,4), repeat=3)))

        while games:
            for p in range(2):
                evo = Counter()
                for state, count in games.items():
                    for roll, variants in dice_rolls.items():
                        next = list(state)
                        next[p*2] = (state[p*2] + roll) % 10
                        next[p*2+1] += next[p*2] + 1
                        if next[p*2+1] >= winning_score:
                            wins[p] += variants * count
                            continue
                        evo[tuple(next)] += variants * count
                games = evo
        return wins.most_common()[0][1]

if __name__ == "__main__":
    Day21().run()
