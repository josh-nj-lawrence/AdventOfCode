import string

class solution():
    def solution(self, filename):
        alphabet = list(string.ascii_lowercase)
        alphabet_upper = list(string.ascii_uppercase)
        # Read input file
        with open(filename) as file:
            lines = file.readlines()
            lines = [item.rstrip() for item in lines]
        score = 0
        groups = [lines[x:x+3] for x in range(0, len(lines), 3)]

        #print(lines)
        for group in groups:
            common = ""
            for c in group[0]:
                if c in group[1] and c in group[2]:
                    common = c
            score += alphabet.index(common)+1 if common in alphabet else alphabet_upper.index(common)+27
        return score


solution = solution()
print(solution.solution("day3_input.txt"))