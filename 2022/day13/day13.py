def evaluate(l,r):
        """
        l: left list of ints input
        r: right list of ints input
        return -1, 1 or 0 if equiv
        """
        if type(l) == int:
            if type(r) == int:
                return l - r
            elif type(r) == list:
                return evaluate([l], r)
        else:
            if type(r) == int:
                return evaluate(l, [r])
        for a, b in zip(l,r):
            # Zip starts if a list runs out
            v = evaluate(a,b)
            if v:
                return v
        # Only gets here if all lengths are equivilent
        return len(l) - len(r)
class solution():    
    def solution(self, filename):
        # Read input file
        with open(filename) as file:
            lines = list(map(str.splitlines, file.read().strip().split("\n\n")))
                     
        # Solution
        t=0
        for i, (a,b) in enumerate(lines):
            if evaluate(eval(a), eval(b)) < 0 :
                t += i + 1
        return t

class solution2():
    def solution(self, filename):
        with open(filename) as file:
            lines = list(map(eval, file.read().split()))

        i2 = 1
        i6 = 2

        for a in lines:
            if evaluate(a, [[2]]) < 0:
                i2 += 1
                i6 += 1
            elif evaluate(a, [[6]]) < 0:
                i6 += 1

        return i2*i6
ans = solution2()
sample = solution2()
print(sample.solution("day13_sample.txt"))
print("\n\n======================\n\n")
print(ans.solution("day13_input.txt"))
