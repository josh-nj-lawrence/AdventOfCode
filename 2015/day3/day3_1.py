class Solution:
    def solution(filename):
        
        with open(filename) as file:
            input = file.readline()
        
        x = 8200
        y = 8200
        p = [[int(0),int(0)] for i in range(0,16400)]
        
        for c in input:
            p[x][y] += 1
            if c == "^":
                y +=1
                p[x][y] +=1
            elif c == "v":
                y -= 1
                p[x][y] +=1
            elif c == ">":
                x += 1
                p[x][y] +=1
            else:
                x -+ 1
                p[x][y] +=1
                
            
        
        # Solve Problem
        
        print(p)
        ans = 0
    
        return ans
solution = Solution
print(solution.solution("day3_input.txt"))