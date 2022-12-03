class solution():
    def solution(self, filename):
        # Read input file
        with open(filename) as file:
            lines = file.readlines()
            lines = [item.rstrip() for item in lines]

        
solution = solution()
print(solution.solution("day2_1_input.txt"))