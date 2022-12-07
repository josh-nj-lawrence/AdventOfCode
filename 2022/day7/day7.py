#Unfinished
class solution():
    def solution(self, filename):
        # Read input file
        with open(filename) as file:
            lines = file.readlines()
            lines = [item.rstrip() for item in lines]
            #lines = [item.split(sep=",") for item in lines]
        
        # Solution    
        current_path = ""
        dirs = {} #List of dirs and their sizes

        # Navigate filesystem and find dirs with 
        max_size = 100000   

        for line in lines:
            print(dirs)
            if line[0] == "$":
                #Process command
                # cd command forward and backward
                if line.split(sep=" ")[1] == "cd": 
                    if line.split(sep=" ")[2] != ".." and line.split(sep=" ")[2] != "/":
                        if current_path != "/":
                            current_path += "/" + line.split(sep=" ")[2]
                        else:
                            current_path += line.split(sep=" ")[2]
                    elif  line.split(sep=" ")[2] == "/":
                        dirs["/"] = 0
                        current_path = "/"
                    elif line.split(sep=" ")[2] == "..":
                        # Cd back
                        current_path = current_path[0:current_path.rfind("/")]
                    else:
                        print(current_path)
                # ls command
                elif line.split(sep=" ")[1] == "ls":
                    pass
                print("Command: " + line + " " + current_path)
                
            elif line.split(sep=" ")[0] == "dir":
                # Is a dir, add to list and 
                if current_path != "/":
                    dir_path = current_path + "/" + line.split(sep=" ")[1]
                else:
                    dir_path = "/" + line.split(sep=" ")[1]
                dirs[dir_path] = 0
                print("Dir: " + line)
            else:
                # Gotta be a file size
                # Update current dir size
                for dir in dirs:
                    if current_path[:len(dir)] == dir and dir != "/":   
                        dirs[current_path] += int(line.split(sep=" ")[0])
                print("File:" + line)
            print(current_path)
        # return num of dirs with less than max_size
        total_size = 0
        for value in dirs.values():
             if value < max_size:
                total_size += value
        return total_size

        
solution = solution()
print(solution.solution("day7_input.txt"))