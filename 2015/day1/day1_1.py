class Solution:
    def solution(self, filename):
        with open(filename) as file:
            input = file.readline()
        chars = list(input)
        floor = 0
        for letter in chars:
            print(letter)
            if letter == "(":
                floor+=1
            else:
                floor-=1
        return floor


solution = Solution()
print(solution.solution("day1_input.txt"))
