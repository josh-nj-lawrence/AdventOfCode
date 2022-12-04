import string

class solution():
    def solution(self, filename):
        
        # Read input file
        with open(filename) as file:
            lines = file.readlines()
            lines = [item.rstrip() for item in lines]
            lines = [item.split(sep=",") for item in lines]
              
        count = 0
        j = 0
        while j < len(lines)-1:
            x1, x2, y1, y2 = 0,0,0,0
            print(lines[j])
            x1, y1 = lines[j][0].split(sep='-')
            x2, y2 = lines[j][1].split(sep="-")

            if int(x1) <= int(x2) and int(y1) >= int(y2):
                #add to count
                print("1)" + x1 + "-" + y1 + " " + x2 +"-" + y2)
                count +=1
            elif int(x1) >= int(x2) and int(y1) <= int(y2):
                print("2)" +x1 +"-" + y1 + " " + x2 +"-" + y2)
                count +=1
            j+=1
        print(count)



solution = solution()
print(solution.solution("day4_input.txt"))