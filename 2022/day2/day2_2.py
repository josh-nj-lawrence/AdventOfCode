class solution():
  def solution(self, filename):
    #Open file
    with open(filename) as file:
      # Read line by line
      lines = file.readlines()
      lines = [item.rstrip() for item in lines]

    # Calculate calories
    calories = 0
    elves = []
    for line in lines:
        if line == "":
            if calories != 0:
              elves.append(calories)
            calories = 0
        else:
          calories += int(line)
          # Edge case for the last line
          if line == lines[len(lines)-1]:
            elves.append(calories)
            calories = 0
    
    # Find top 3 for total calories
    tot_calories = 0
    for i in range(3):
        tot_calories += max(elves)
        elves.remove(max(elves))
    
    # Return elf with max calories
    return(tot_calories)

solution = solution()
print(solution.solution("day1_1_input.txt"))