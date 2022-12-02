class solution():
    def solution(self, filename):
        # Read input file
        with open(filename) as file:
            lines = file.readlines()
            lines = [item.rstrip() for item in lines]

        # Set up score dict
        scores = {
            "A": 1,
            "B": 2,
            "C": 3,
            "X": 1, #Rock
            "Y": 2, #Paper
            "Z": 3 #Scissors
        }
        wins = ["A Y","B Z","C X"]
        ties = ["A X","B Y","C Z"]
        losses = ["B X","C Y","A Z"]
        score = 0

        # iterate through input and determine winner, add score to score total
        for line in lines:
            print(line + " : " + str(score))
            if line in wins:
                score += 6 + scores.get(line[2])
            elif line in ties:
                score += 3 + scores.get(line[2])
            elif line in losses:
                score += scores.get(line[2])
        return score

solution = solution()
print(solution.solution("day2_1_input.txt"))