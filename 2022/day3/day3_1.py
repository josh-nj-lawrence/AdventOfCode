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
        for line in lines:
            # Split into compartments
            comp1 = line[:len(line)//2]
            comp2 = line[(len(line)//2):]
            
            # find common elements
            common = ""
            for c in comp1:
                if c in comp2:
                    common = c
            if common in alphabet_upper:
                score += alphabet_upper.index(common) + 27
            else:
                score += alphabet.index(common) + 1
            
            # Add common scores
        return score
        


solution = solution()
print(solution.solution("day3_input.txt"))