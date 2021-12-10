from aoc2021 import Day

pts={ ")":3, "]":57, "}":1197, ">":25137 }
opening=["(", "[", "{", "<"]
closing=[")", "]", "}", ">"]
braces={ ")":"(", "]":"[", "}":"{", ">":"<"}


class Day10(Day):
    def get_test_input(self):
        return ["[({(<(())[]>[[{[]{<()<>>",
                "[(()[<>])]({[<{<<[]>>(",
                "{([(<{}[<>[]}>{[]{[(<()>",
                "(((({<>}<{<{<>}{[]{[]{}",
                "[[<[([]))<([[{}[[()]]]",
                "[{[{({}]{}}([{[{{{}}([]",
                "{<[[]]>}<{[{[{[]{()[[[]",
                "[<(<(<(<{}))><([]([]()",
                "<{([([[(<>()){}]>(<<{{",
                "<{([{{}}[<[[[<>{}]]]>[]]"]
    
    def a(self):
        first_illegal=[]
        for line in self.puzzle_input:
            stack = []
            for char in line:
                if char in braces.values():
                    stack.append(char)
                elif char in braces:
                    expected = stack.pop()
                    if braces[char] != expected:
                        first_illegal.append(char)
                        break
        return sum([pts[x]for x in first_illegal])


    def b(self):
        pass

if __name__ == "__main__":
    Day10().run()