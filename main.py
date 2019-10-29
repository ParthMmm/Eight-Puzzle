

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


def main():

    choosePuzzle = input(
        "Welcome to Parth Mangrola's 8-puzzle solver. Type 1 to use a default puzzle, or 2 to enter your own puzzle." '\n')

    if choosePuzzle == "1":  # default puzzle
        print("default selected")

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




main()
