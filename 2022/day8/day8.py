#Unfinished
class solution():
    def solution(self, filename):
        # Read input file
        with open(filename) as file:
            lines = file.readlines()
            lines = [list(item.rstrip()) for item in lines]
            #lines = [item.split(sep="") for item in lines]

        # Solution
        visible_trees = 0
        count = 0
        max_score = 0
        # Itter over rows
        for i in range(len(lines)):
            # Itter over columns
            for j in range(len(lines[i])):
                up_dis, down_dis, left_dis, right_dis = 0,0,0,0
                # Hit each value
                if i == 0 or i == len(lines)-1:
                    # Top or bottom row
                    visible_trees += 1
                elif j == 0 or j == len(lines[i])-1:
                    # Left or right columns
                    visible_trees += 1
                else:
                    # Check vertical visibility
                    up_vert_true = True
                    down_vert_true = True
                    # Look up
                    for y in reversed(range(i)):
                        #print(str(y) + " stop")
                        if lines[i][j] > lines[y][j]:
                            up_dis += 1
                        else:
                            if lines[i][j] == lines[y][j]:
                                up_dis += 1
                            up_vert_true = False
                    # Look down
                    for y in range(i+1, len(lines)):
                        if not down_vert_true:
                            #print("break")
                            break
                        if lines[i][j] > lines[y][j]:
                            down_dis += 1
                        else:
                            if lines[i][j] == lines[y][j]:
                                down_dis += 1
                            down_vert_true = False                   

                    # Check horozontal visibility
                    l_horo_true = True
                    r_horo_true = True
                    # Look left
                    for x in reversed(range(j)):
                        #print(x)
                        if lines[i][j] > lines[i][x]:
                            left_dis += 1
                        else:
                            if lines[i][j] == lines[i][x]:
                                left_dis += 1
                            l_horo_true = False
                    # Look right
                    for x in range(j+1, len(lines)):
                        if not r_horo_true:
                            #print("break")
                            break
                        #print(x)
                        if lines[i][j] > lines[i][x]:
                            right_dis += 1
                        else:
                            #if lines[i][j] == lines[i][x]:
                                #right_dis += 1
                            r_horo_true = False   
                    if up_vert_true or down_vert_true or l_horo_true or r_horo_true:
                        count += 1
                if left_dis*right_dis*up_dis*down_dis > max_score:
                    max_l, max_r, max_up, max_down = left_dis, right_dis, up_dis, down_dis
                    max_score = left_dis*right_dis*up_dis*down_dis
                    print(max_l, max_r, max_up, max_down)
                    print(lines[i][j], i, j)
        print("visible: " + str(visible_trees) + " other: " + str(count) + " Total: " + str(visible_trees + count) + " Max Score: " + str(max_score))

        return True

        
solution = solution()
print(solution.solution("day8_input.txt"))

# 5232240
# 5755197