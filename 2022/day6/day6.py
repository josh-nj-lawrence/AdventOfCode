class solution():
    def solution(self, filename):
        # Read input file
        with open(filename) as file:
            line = file.readline()
            #lines = [item.rstrip() for item in lines]
        subline_len = 14
        # Solution
        for i in range (0, len(line)-subline_len-1):
            print(line[i:i+subline_len])
            count = 0
            for j in line[i:i+subline_len]:
                subline = line[i:i+subline_len].replace(j, "", 1)
                print(subline)
                if j not in subline: 
                    count+=1
            if count == subline_len:
                return i+subline_len
                
            
        
solution = solution()
print(solution.solution("day6_input.txt"))