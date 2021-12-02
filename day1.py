class solution():
  def number_of_depth_increase(input):
    count = 0
    for i, val in enumurate(input):
      if input[i+1] > val:
        count += 1
    return count
  
input = [10, 20, 30, 40, 50, 30, 40]

result = solution()
print(result.number_of_depth_increase(input))
