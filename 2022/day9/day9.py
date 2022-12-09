#Unfinished
class solution():
    def solution(self, filename):
        # Read input file
        with open(filename) as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]

        # Solution
        #Define dict of hisorical tail positions
        visited = {}

        # Define head and tail position vars
        headx, heady = 0,0
        tailx, taily = 0,0

        #Loop over instructions, move head and move tail
        last_dir = ""
        for line in lines:
            dir = line.split()[0] 
            for i in range(int(line.split()[1])):
                # Vertical
                if dir == "U":
                    taily = heady
                    heady += 1
                    visited[tailx,taily] = 1
                    
                elif dir == "D":
                    taily = heady
                    heady -= 1
                    if last_dir == "L" or last_dir == "R":
                        visited[tailx,taily] = 1
                    
                # Horozontal
                elif dir == "L":
                    tailx = headx
                    headx -= 1
                    if last_dir == "U" or last_dir == "D":
                        visited[tailx,taily] = 1
                    
                else:
                    # Right
                    tailx = headx
                    headx += 1
                    if last_dir == "U" or last_dir == "D":
                        visited[tailx,taily] = 1
                    
            last_dir = dir
        # Update Mapping
        print(visited)
        return len(visited)
        
solution = solution()
print(solution.solution("day9_input.txt"))

#6582