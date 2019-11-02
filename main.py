

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


def algorithm_chooser(puzzle):

    choose_algorithm = input("Enter your choice of algorithm:" '\n'
                            "1. Uniform Cost Search" '\n'
                            "2. A* with Misplaced Tile heuristic" '\n'
                            "3. A* with the Manhattan distance heuristic" '\n')
    if choose_algorithm == "1":
        heuristic = 0
    if choose_algorithm == "2":
        heuristic = misplaced_tile(puzzle)
        print("Misplaced tiles: " + str(heuristic) + '\n')
    if choose_algorithm == "3":
        heuristic = manhattan_distance(puzzle)
        print("Manhattan distance is: " + str(heuristic) + '\n')


# Compare puzzle with goal and count the diff
def misplaced_tile(puzzle):
    h = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != goal_state[i][j]:
                h += 1
    return h

#Compare position of puzzle_num to goal_num and calculate distance
#Sum is manhattan_distance
def manhattan_distance(puzzle):
    h = 0
    for i in range(3):
        for j in range(3):
            puzzle_num = puzzle[i][j]
            goal_num = goal_state[i][j]

            x = abs((puzzle_num / 3) - (goal_num / 3))
            y = abs((puzzle_num % 3) - (goal_num % 3))

            h += (x + y)
    return int(h)


def main():

    choose_puzzle = input(
        "Welcome to Parth Mangrola's 8-puzzle solver. Type 1 to use a default puzzle, or 2 to enter your own puzzle." '\n')

    if choose_puzzle == "1":  # default puzzle
        choose_default = input("Choose one of the following:" '\n'
                              "1. Trivial Puzzle" '\n'
                              "2. Easy Puzzle" '\n'
                              "3. Oh Boy Puzzle" '\n'
                              "4. Very Easy Puzzle" '\n'
                              "5. Doable Puzzle" '\n'
                              "6. Impossible Puzzle" '\n')
        if choose_default == "1":
            print("Trivial selected" '\n')
            print(trivial_case)
            algorithm_chooser(trivial_case)

        if choose_default == "2":
            print("Easy selected" '\n')
            print(easy_case)
            print('\n')
            algorithm_chooser(easy_case)

        if choose_default == "3":
            print("Oh Boy selected" '\n')
            print(ohBoy_case)
            algorithm_chooser(ohBoy_case)

        if choose_default == "4":
            print("Very Easy selected" '\n')
            print(veryEasy_case)
            algorithm_chooser(veryEasy_case)

        if choose_default == "5":
            print("Doable selected" '\n')
            print(doable_case)
            algorithm_chooser(doable_case)

        if choose_default == "6":
            print("Impossible selected" '\n')
            print(impossible_case)
            algorithm_chooser(impossible_case)

    if choose_puzzle == "2":  # custom puzzle

        print("Enter your puzzle, use a zero to represent the blank." '\n')

        row_one = input("Enter the first row, use space between numbers." '\n')

        row_two = input("Enter the second row, use space between numbers." '\n')

        row_three = input(
            "Enter the third row, use space between numbers." '\n')

        row_one = [int(i) for i in row_one.split(" ")]
        row_two = [int(i) for i in row_two.split(" ")]
        row_three = [int(i) for i in row_three.split(" ")]

        custom_puzzle = [row_one, row_two, row_three]

        print(custom_puzzle)

        algorithm_chooser(custom_puzzle)


main()
