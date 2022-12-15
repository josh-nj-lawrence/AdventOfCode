class solution():    
    def solution(self, filename):
        # Read input file
        with open(filename) as file:
            lines = file.readlines()
            lines = [line.rstrip().strip().split(" -> ") for line in lines]
            #lines = [itm.split(",") for line in lines for itm in line]
                     
        # Solution
        # Define cave scan
        rocks = [] # x,y points which represent rocks in the scan
        #for line in lines:


        # Fall sand until it falls to void
        return lines

ans = solution()
sample = solution()
print(sample.solution("day14_sample.txt"))
print("\n======================\n")
#print(ans.solution("day14_input.txt"))
