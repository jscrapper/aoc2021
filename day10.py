from aoc2021 import Day

err_pts={ ")":3, "]":57, "}":1197, ">":25137 }
complete_pts={ ")":1, "]":2, "}":3, ">":4 }
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
        return sum([err_pts[x]for x in first_illegal])


    def b(self):
        # filter only valid lines
        valid_lines = []
        tails=[]
        scores=[]
        for line in self.puzzle_input:
            stack=[]
            isValid=True
            for char in line:
                if char in opening:
                    stack.append(char)
                elif char in closing:
                    expected=closing[opening.index(stack.pop())]
                    if char != expected:
                        isValid=False
                        break
            if isValid: 
                # completed the line without failing. if there's still a stack, complete it. 
                tail=""
                score=0
                while len(stack) > 0:
                    char = stack.pop()
                    close = closing[opening.index(char)]
                    tail += close
                    score = score * 5 + complete_pts[close]
                valid_lines.append(line)
                tails.append(tail)
                scores.append(score)
        middle_score = sorted(scores)[int((len(scores)-1)/2)]
        return middle_score


if __name__ == "__main__":
    Day10().run()