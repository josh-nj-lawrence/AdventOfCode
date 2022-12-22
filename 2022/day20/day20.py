def shift_ele(arr, ele):
    # Find OG Index
    i = arr.index(ele)
    # Find new index
    shift = ele%(len(arr)+1)

class solution():    
    def solution(self, filename):
        # Read input file
        with open(filename) as file:
            lines = file.readlines()
            lines = [int(line.rstrip()) for line in lines]
            #lines = [itm.split(",") for line in lines for itm in line]
                     
        # Solution
        mixed = lines
        for ele in lines:
            # Move ele to new position
            pass
        return lines

ans = solution()
sample = solution()
print(sample.solution("day20_sample.txt"))
print("\n======================\n")
#print(ans.solution("day20_input.txt"))
