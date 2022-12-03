class Solution:
    def solution(filename):
        with open(filename) as file:
            lines = file.readlines()
        tot_ribbon = 0
        # Solve Problem
        for line in lines:
            spare = 0
            # Split into 3 measurements
            m = line.strip("\n").split(sep="x")
            m = [int(i) for i in m]
            
            #calculate sides and spare
            spare = int(m[0])*int(m[1])*int(m[2])
            m.remove(max(m))

            #calculate total
            tot_ribbon += 2*int(m[0]) + 2*int(m[1]) + int(spare)
        return tot_ribbon
solution = Solution
print(solution.solution("day2_input.txt"))