class solution():    
    def solution(self, filename):
        # Read input file
        with open(filename) as file:
            lines = file.readlines()
            lines = [line.rstrip().strip().split(" -> ") for line in lines]
            #lines = [itm.split(",") for line in lines for itm in line]
                     
        # Solution
     
        return lines

ans = solution()
sample = solution()
print(sample.solution("day15_sample.txt"))
print("\n======================\n")
#print(ans.solution("day15_input.txt"))
