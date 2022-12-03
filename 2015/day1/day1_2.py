class Solution:
    def solution(self, filename):
        with open(filename) as file:
            input = file.readline()
        chars = list(input)
        floor = 0
        entry = 0
        for i, letter in enumerate(chars):
            
            if letter == "(":
                floor+=1
            else:
                floor-=1
            # Check if entered the basement
            if floor < 0:
                entry = i+1
                return entry
        return -1


solution = Solution()
print(solution.solution("day1_input.txt"))
