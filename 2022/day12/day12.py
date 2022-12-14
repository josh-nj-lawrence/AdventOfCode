# Not complete
class solution():
    def solution(self, filename):
        # Read input file
        with open(filename) as file:
            lines = file.readlines()
            lines = [line.rstrip().strip() for line in lines]
         
        # Solution
        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        r, c = [r for r, line in enumerate(lines) for c, character in enumerate(line) if character == "S"], [c for r, line in enumerate(lines) for c, character in enumerate(line) if character == "S"]
        chr = lines[r[0]][c[0]]
        r, c = [r for r, line in enumerate(lines) for c, character in enumerate(line) if character == "E"], [c for r, line in enumerate(lines) for c, character in enumerate(line) if character == "E"]
        dest = lines[r[0]][c[0]]
        while chr is not "E":
            # Look each direction if theres a step up take it, else step toward dest 
            pass
        return lines

ans = solution()
sample = solution()
print(sample.solution("day12_sample.txt"))
print("\n\n======================\n\n")
print(ans.solution("day12_input.txt"))
