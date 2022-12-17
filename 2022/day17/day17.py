def addRock(chamber, rock):
        """
            chamber: h x 7 array of stationary rocks and moving rocks
            rock: rock to be added to the chamber
        """
        # Find heights stationary rock (or floor)
        heighest_rock = 0
        for i,row in enumerate(reversed(chamber)):
            # itter vertically from top down
            for c in row:
                if c == "#":
                    # Return row index for height 
                    heighest_rock = (len(chamber)-1) - i
        print(heighest_rock)

        # Find size of rock
        h, w = len(rock), len(rock[0])

        # Add rock
        # Add lines if needed
        if len(chamber) - heighest_rock >= 4:
            chamber += ['.'*7]*h
        # Add rock in new lines
        for r in reversed(range(len(chamber)-h,len(chamber))):
            pass
            """chamber[r] = 
                for c in range(w):
                chamber[r] """
        str=""
        #chamber[len(chamber)-1] = "."*int((7-len(rock))/2) + str.join(rock) + "."*int((7-len(rock))/2)


class solution():  
    def solution(self, filename):
        # Read input file
        with open(filename) as file:
            line = file.readlines()
            moves = [c for c in line[0]]
            #lines = [line.rstrip().strip().split(" -> ") for line in lines]
            #lines = [itm.split(",") for line in lines for itm in line]
                     
        # Solution
        # Build list of rocks
        rocks = [
            ['@','@','@'], # Horoz Line
            [['.','@','.'],['@','@','@'],['.','@','.']], #Plus
            [['.','.','@'],['.','.','@'],['@','@','@']], # Backwards L
            [['@'],['@'],['@'],['@']], # Vert Line
            [['@','@'],['@','@']] # Square
        ]
        # Build chamber
        chamber = ['#'*7]
        chamber += ['.'*7]*3# for _ in range(7)]*4

        # Test manipulating chamber to add new rock
        addRock(chamber, rocks[1])
        

        # Display Chamber
        for row in reversed(chamber):
            print(row)

        return ""

ans = solution()
sample = solution()
print(sample.solution("day17_sample.txt"))
print("\n======================\n")
#print(ans.solution("day17_input.txt"))
