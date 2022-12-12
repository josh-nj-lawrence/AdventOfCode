# Not finished at all
class solution():
    def solution(self, filename):
        # Read input file
        with open(filename) as file:
            lines = file.readlines()
            lines = [line.rstrip().strip() for line in lines]
        # Convert input into List of Monkeys
        #monkeys = [group for lines[i:i+7] in lines]

class solution2():
    def solution(self, filename):
        # Read input file
        with open(filename) as file:
            lines = file.readlines()
            lines = [line.rstrip().strip() for line in lines]
        # Convert input into List of Monkeys
        monkeys = [lines[i:i+6] for i in range(0,len(lines), 7)]
        for i in range(len(monkeys)):
            monkeys[i][0] = int(monkeys[i][0][7]) # Monkey Index
            monkeys[i][1] = [int(j) for j in list(monkeys[i][1][16:].split(sep=","))] # Items List
            monkeys[i][2] = list(monkeys[i][2][21:].split(sep=" ")) # Operations
            monkeys[i][3] = int(monkeys[i][3][18:]) # Divisible by
            monkeys[i][4] = int(monkeys[i][4][-1]) # monkey index to throw if true
            monkeys[i][5] = int(monkeys[i][5][-1]) # monkey index to throw if false
        print(monkeys)
        # Solution
        # Loop 20 rounds
        rounds = 20
        for _ in range(rounds):
            # Process one round
            for m in monkeys:
                # Take a turn
                # Loop over each item
                for h, i in enumerate(m[1]):
                    # Look at item and increase worry by operation
                    if m[2][0] == "+":
                        # Add val
                        m[1][h] += int(m[2][1])
                    else:
                        # Squared
                        if m[2][1] == "old":
                            m[1][h] = m[1][h]**2 
                        else:
                            # Multiply by val
                            m[1][h] = m[1][h] * int(m[2][1])
                        
                    # Feel Relieved
                    m[1][h] = m[1][h]//3
                    # Test Operation
                    if m[1][h] % m[3] == 0:
                        # Throw item to true option
                        monkeys[m[4]][1].append(m[1][h])
                        m[1].remove(m[1][h])
                    else:
                        # Throw item to false option
                        pass
 
        return monkeys

ans = solution2()
sample = solution2()
print(sample.solution("day11_sample.txt"))
print("\n\n======================\n\n")
print(ans.solution("day11_input.txt"))
