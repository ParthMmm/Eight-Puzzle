

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

trivial_case = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 0]]

easy_case = [[1, 2, 0],
             [4, 5, 3],
             [7, 8, 6]]

ohBoy_case = [[8, 7, 1],
              [6, 0, 2],
              [5, 4, 3]]

veryEasy_case = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 0, 8]]

doable_case = [[0, 1, 2],
               [4, 5, 3],
               [7, 8, 6]]

impossible_case = [[1, 2, 3],
                   [4, 5, 6],
                   [8, 7, 0]]




def algorithmChooser(puzzle):

    chooseAlgorithm = input("Enter your choice of algorithm:" '\n'
                            "1. Uniform Cost Search" '\n'
                            "2. A* with Misplaced Tile heuristic" '\n'
                            "3. A* with the Manhattan distance heuristic" '\n')
    if chooseAlgorithm == "1":
        search(puzzle, 0)
    if chooseAlgorithm == "2":
        search(puzzle, 1)
    if chooseAlgorithm == "3":
        search(puzzle, 2)

def search(puzzle, heurisitic):
    print("todo")

def main():

    choosePuzzle = input(
        "Welcome to Parth Mangrola's 8-puzzle solver. Type 1 to use a default puzzle, or 2 to enter your own puzzle." '\n')

    if choosePuzzle == "1":  # default puzzle
        chooseDefault = input("Choose one of the following:" '\n'
              "1. Trivial Puzzle" '\n'
              "2. Easy Puzzle" '\n'
              "3. Oh Boy Puzzle" '\n'
              "4. Very Easy Puzzle" '\n'
              "5. Doable Puzzle" '\n'
              "6. Impossible Puzzle" '\n')
        if chooseDefault == "1":
            print("Trivial selected" '\n')
            print(trivial_case)
            algorithmChooser(trivial_case)

        if chooseDefault == "2":
            print("Easy selected" '\n')
            print(easy_case)
            algorithmChooser(easy_case)

        if chooseDefault == "3":
            print("Oh Boy selected" '\n')
            print(ohBoy_case)
            algorithmChooser(ohBoy_case)

        if chooseDefault == "4":
            print("Very Easy selected" '\n')
            print(veryEasy_case)
            algorithmChooser(veryEasy_case)

        if chooseDefault == "5":
            print("Doable selected" '\n')
            print(doable_case)
            algorithmChooser(doable_case)

        if chooseDefault == "6":
            print("Impossible selected" '\n')
            print(impossible_case)
            algorithmChooser(impossible_case)


    if choosePuzzle == "2":  # custom puzzle

        print("Enter your puzzle, use a zero to represent the blank." '\n')

        rowOne = input("Enter the first row, use space between numbers." '\n')

        rowTwo = input("Enter the second row, use space between numbers." '\n')

        rowThree = input("Enter the third row, use space between numbers." '\n')

        rowOne = [int(i) for i in rowOne.split(" ")]
        rowTwo = [int(i) for i in rowTwo.split(" ")]
        rowThree = [int(i) for i in rowThree.split(" ")]

        customPuzzle = [rowOne, rowTwo, rowThree]

        print(customPuzzle)

        algorithmChooser(customPuzzle)

main()
