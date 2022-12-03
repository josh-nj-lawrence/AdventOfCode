from collections import deque

class Solution:
    def solution(filename):
        with open(filename) as file:
            line = file.readline().split(sep=", ")
        
        # Solve Problem
        x,y = 0,0
        directions = deque(["N","W","S","E"])
        dir = "N"
        for i in line:
            #Change direction
            [directions.rotate(1) if i[0] =="R" else directions.rotate(-1)]
            dir = directions[1] 

            # Move
            if dir == "E":
                x += int(i[1:])
            elif dir == "W":
                x -= int(i[1:])
            elif dir == "N":
                y += int(i[1:])
            else:
                y -= int(i[1:])
        
        print(line)
        return x + y
solution = Solution
print(solution.solution("day1_input.txt"))