"""
  Notes:
    - need 50 stars by Dec 25th
    - collect starts by solving puzzles.
"""
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
    

    # Return elf with max calories
    return(max(elves))
  """   print(max(elves)) 
    print(lines) """


solution = solution()
print(solution.solution("day1_input.txt"))
