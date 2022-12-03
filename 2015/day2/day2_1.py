class Solution:
    def solution(filename):
        with open(filename) as file:
            lines = file.readlines()
        tot_wrapping = 0
        # Solve Problem
        for line in lines:
            spare = 0
            # Split into 3 measurements
            m = line.strip("\n").split(sep="x")
            print(m)
            #calculate sides 
            spare = min([int(m[0])*int(m[1]), int(m[1])*int(m[2]), int(m[2])*int(m[0])])
            print(spare)
            # Calulcate SA + spare
            tot_wrapping += 2*int(m[0])*int(m[1]) + 2*int(m[1])*int(m[2]) + 2*int(m[2])*int(m[0]) + int(spare)

        return tot_wrapping
solution = Solution
print(solution.solution("day2_input.txt"))