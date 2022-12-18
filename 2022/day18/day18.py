def get_input(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip().strip().split() for line in lines]
        lines = [itm.split(",") for line in lines for itm in line]
    return lines

def add_sides(coord):
    edges = []
    edges.append([coord[0]+1, coord[1], coord[2]])
    edges.append([coord[0]-1, coord[1], coord[2]])
    edges.append([coord[0], coord[1]+1, coord[2]])
    edges.append([coord[0], coord[1]-1, coord[2]])
    edges.append([coord[0], coord[1], coord[2]+1])
    edges.append([coord[0], coord[1], coord[2]-1])

class solution():  
    def solution(self, filename):
        # Read input file
        coords = get_input(filename)

        # Solution     

        return coords

ans = solution()
sample = solution()
print(sample.solution("day18_sample.txt"))
print("\n======================\n")
#print(ans.solution("day18_input.txt"))
