#Very much not done
import string

class solution():
    def solution(self, filename):
        # Read input file
        with open(filename) as file:
            lines = file.readlines()
            lines = [item.rstrip() for item in lines]
            lines = [item.split(sep=",") for item in lines]

        # J is columns, i is rows
        crates=[]
        for i in reversed(range(0,8)):
            for j in range (0,8):
                # Add crates to array for later manipulation with crate movement
                pass

solution = solution()
print(solution.solution("day5_input.txt"))