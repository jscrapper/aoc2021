import itertools
from aoc2021 import Day
from itertools import permutations

class Base:
    def __init__(self, depth, parent ):
        self.depth = depth
        self.parent = parent
    
    @property
    def is_left(self):
        return None if self.parent is None else self.parent.left == self

    @property
    def dir(self):
        return "left" if self.is_left else "right"

    def add_to_leaf(self, value, dir):
        return NotImplemented

    def explode(self):
        return NotImplemented

    def split(self):
        return NotImplemented

class Leaf(Base):
    def __init__(self, value:int, depth:int, parent):
        super().__init__(depth, parent)
        self._value = value

    @property
    def value(self):
        return self._value

    def explode(self):
        return False
    
    def split(self):
        if self.value < 10:
            return False

        n = self.value
        self.parent.add_child([n // 2, n // 2 + n % 2], self.dir)
        return True

    def __repr__(self):
        return str(self.value)

    def add_to_leaf(self, value, dir):
        """add all the way down"""
        self._value += value

    @property
    def magnitude(self):
        return self._value

class Branch(Base):
    def __init__(self, value:list, depth:int=0, parent=None):
        super().__init__(depth, parent)
        for i,dir in enumerate(("left","right")):
            # cls=Leaf if isinstance(value[i], int) else Branch
            # setattr(self, dir, cls(value[i], depth+1, self))
            self.add_child(value[i], dir)

    @property
    def value(self):
        return [self.left.value, self.right.value]

    def child(self, dir):
        return self.__getattribute__(dir)

    def add_child(self, value, dir):
        cls=Leaf if isinstance(value, int) else Branch
        setattr(self, dir, cls(value, self.depth+1, self))

    def find_parent(self, dir):
        current=self
        parent = current.parent
        while parent:
            if dir != current.dir: # right if left, left if right
                return parent
            current = parent
            parent = current.parent

    def add_to_leaf(self, value, dir):
        return self.child(dir).add_to_leaf(value, dir)

    def explode(self):
        if self.depth < 4:
            return self.left.explode() or self.right.explode()

        # do explode
        for dir in ("left", "right"):
            parent = self.find_parent(dir)
            if parent:
                flip="right" if dir == "left" else "left"
                parent.child(dir).add_to_leaf(self.child(dir).value, flip)
                
        self.parent.add_child(0, self.dir)
        return True
        
        
    def split(self) -> bool:
        return self.left.split() or self.right.split()

    def reduce(self):
        # recurse explode then recurse split. 
        while True:
            exploded = False

    def __repr__(self):
        return f"<{self.left},{self.right}>"

    @property
    def magnitude(self):
        return self.left.magnitude * 3 + self.right.magnitude * 2

    def combine(self, other):
        self.left = Branch(self.value, 1, self)
        self.right = Branch(other.value, 1, self)
        while self.explode() or self.split():
            continue
        return self

    @classmethod
    def add(cls, a, b):
        r=cls([a.value,b.value], 0, None)
        while r.explode() or r.split():
            continue
        return r


class Day18(Day):
    def get_test_input(self):
        return ["[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
                "[[[5,[2,8]],4],[5,[[9,9],0]]]",
                "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]",
                "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]",
                "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]",
                "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]",
                "[[[[5,4],[7,7]],8],[[8,3],8]]",
                "[[9,3],[[9,9],[6,[4,9]]]]",
                "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
                "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"]
    
    def parse_input(self):
        # make sure to ignore the opening brace for the root
        return [Branch(eval(x)) for x in self.raw_puzzle_input]

    def a(self):
        tree = self.puzzle_input[0]
        for branch in self.puzzle_input[1:]:
            tree.combine(branch)
        return tree.magnitude

    def b(self):
        result = 0
        li=lj=first=second=largest=None

        for x in permutations(range(len(self.puzzle_input)), 2):
            if x[0] == x[1]: 
                continue
            a=self.puzzle_input[x[0]]
            b=self.puzzle_input[x[1]]
            s = Branch.add(a,b)
            if s.magnitude > result:
                li=x[0]
                lj=x[1]
                largest = s
                result = s.magnitude
                first = a
                second = b
        return result


if __name__ == "__main__":
    Day18().run(force_reparse=True)