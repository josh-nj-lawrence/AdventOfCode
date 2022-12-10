def is_sprite_visible(x, c):
  return abs(x - (c-1) % 40) < 2

class solution2():
    def solution(self, filename):
        # Read input file
        with open(filename) as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]

        # Solution
        x = 1 # cpu value
        c = 1 # Cycle number
        sum = 0
        cycles = [x for x in range(20, 221, 40)]
        line_return = [x for x in range(40, 240, 40)]
    
        for line in lines:
            try:
                op, val = line.split()
            except ValueError:
                #Noop
                op = line.split()[0]
            
            # Update location based on operation
            # Val to itter if c += 2 allows us to draw CRT 1 per cycle
            itter = True
            i = 0
            while itter:
                # Draw CRT
                if c in line_return:
                    # Return line
                    print("")
                    pass
                else:
                    if is_sprite_visible(x, c):
                        print("#", end="")
                    else:
                        print(".", end="")
                if op == "addx":
                    i+=1
                    if i == 2:
                        # Add value to register
                        x += int(val)
                        itter = False
                    c+=1
                else:
                    # Noop Operation
                    c+=1
                    itter = False
                # Add to sum
                if c in cycles:
                    sum += x*c       
        return sum

ans = solution2()
sample = solution2()
print(sample.solution("day10_sample.txt"))
print("======================")
print(ans.solution("day10_input.txt"))
