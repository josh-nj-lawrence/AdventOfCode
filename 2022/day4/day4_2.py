import re
class solution():
    def solution(self, filename):
        
        with open("day4_input.txt") as input_file:
            lines = input_file.readlines()

        pairs = [[int(i) for i in re.split(',|-',l.strip())] for l in lines]
        overlaps = [(a<=c and d<=b) or (c<=a and b<=d) for a,b,c,d in pairs]
        semi_overlaps = [not ((b<c) or (d<a)) for a,b,c,d in pairs]
        #print(sum(overlaps))
        #print(sum(semi_overlaps))
        return sum(semi_overlaps)

solution = solution()
print(solution.solution("day4_input.txt"))
