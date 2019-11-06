from heapq import heapify, heappush, heappop
from copy import deepcopy

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


class Node:
    def __init__(self, puzzle, heuristic, depth):
        self.puzzle = puzzle
        self.h = heuristic
        self.g = depth
        self.f = heuristic + depth

    def __lt__(self, other):
        return self.f < other.f


def algorithm_chooser(puzzle):

    choose_algorithm = input("Enter your choice of algorithm:" '\n'
                             "1. Uniform Cost Search" '\n'
                             "2. A* with Misplaced Tile heuristic" '\n'
                             "3. A* with the Manhattan distance heuristic" '\n')
    if choose_algorithm == "1":
        h = 1
        search(puzzle, h)
    if choose_algorithm == "2":
        h = 2
        search(puzzle, h)
    if choose_algorithm == "3":
        h = 3
        search(puzzle, h)


# Compare puzzle with goal and count the diff
def misplaced_tile(puzzle):
    h = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != 0:
                if puzzle[i][j] != goal_state[i][j]:
                    h += 1
    return h


def manhattan_distance(puzzle):
    h = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != 0:

                x = ((puzzle[i][j] - 1) // 3)
                y = ((puzzle[i][j] - 1) % 3)

                h += abs(x - i) + abs(y - j)

    return int(h)


def print_puzzle(puzzle):
    for i in range(3):
        print(puzzle[i])
    print('\n')


def search(puzzle, h):
    open_list = []
    total_nodes_expanded = 0
    max_nodes_queue = 0
    depth_goal = 0
    solved = 0

    if h == 1:
        heuristic = 0
    if h == 2:
        heuristic = misplaced_tile(puzzle)
    if h == 3:
        heuristic = manhattan_distance(puzzle)

    start_node = Node(puzzle, heuristic, 0)
    heappush(open_list, start_node)

    while(open_list):

        heapify(open_list)

        # only update if open_list is larger
        if max_nodes_queue < len(open_list):
            max_nodes_queue = len(open_list)

        tmp = heappop(open_list)

        print("Best state to expand g(n) = " +
              str(tmp.g) + " h(n) = " + str(tmp.h) + '\n')

        print_puzzle(tmp.puzzle)

        if(is_solved(tmp.puzzle)):  # check if goal else expand
            solved = 1
            break

        new_list, total_nodes_expanded = move_tiles(tmp, total_nodes_expanded)

        # update nodes
        for i in range(len(new_list)):
            if h == 1:
                new_list[i].h = 0
            if h == 2:
                new_list[i].h = misplaced_tile(new_list[i].puzzle)
                new_list[i].f = new_list[i].g + new_list[i].h
            if h == 3:
                new_list[i].h = manhattan_distance(new_list[i].puzzle)
                new_list[i].f = new_list[i].g + new_list[i].h
            heappush(open_list, new_list[i])

    if(solved):
        print("Solved!" + '\n')
        print_puzzle(tmp.puzzle)

        print("To solve this problem the search algorithm expanded " +
              str(total_nodes_expanded) + " nodes." + '\n')
        print("The maximum number of nodes in the queue at any one time was " +
              str(max_nodes_queue) + '.' + '\n')
        print("The depth of the goal node was " + str(tmp.g) + '.' + '\n')


def is_solved(puzzle):
    if(puzzle == goal_state):
        return 1
    else:
        return 0

# pass in current node and total_nodes_expanded to update


def move_tiles(n, total_nodes_expanded):
    # find 0 so we know where we can move

    for i in range(3):
        for j in range(3):
            if n.puzzle[i][j] == 0:
                x = i
                y = j

    temp_list = []
    if x > 0:  # down
        copy_list = deepcopy(n.puzzle)
        copy_list[x][y] = copy_list[x - 1][y]
        copy_list[x - 1][y] = 0
        new_node = Node(copy_list, 0, n.g + 1)
        temp_list.append(new_node)
        total_nodes_expanded += 1

    if x < 2:  # up
        copy_list = deepcopy(n.puzzle)
        copy_list[x][y] = copy_list[x + 1][y]
        copy_list[x + 1][y] = 0
        new_node = Node(copy_list, 0, n.g + 1)
        temp_list.append(new_node)
        total_nodes_expanded += 1

    if y > 0:  # left

        copy_list = deepcopy(n.puzzle)
        copy_list[x][y] = copy_list[x][y - 1]
        copy_list[x][y - 1] = 0

        new_node = Node(copy_list, 0, n.g + 1)
        temp_list.append(new_node)
        total_nodes_expanded += 1

    if y < 2:  # right
        copy_list = deepcopy(n.puzzle)
        copy_list[x][y] = copy_list[x][y + 1]
        copy_list[x][y + 1] = 0
        new_node = Node(copy_list, 0, n.g + 1)
        temp_list.append(new_node)
        total_nodes_expanded += 1

    return temp_list, total_nodes_expanded


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
            print_puzzle(trivial_case)
            algorithm_chooser(trivial_case)

        if choose_default == "2":
            print("Easy selected" '\n')
            print_puzzle(easy_case)
            algorithm_chooser(easy_case)

        if choose_default == "3":
            print("Oh Boy selected" '\n')
            print_puzzle(ohBoy_case)
            algorithm_chooser(ohBoy_case)

        if choose_default == "4":
            print("Very Easy selected" '\n')
            print_puzzle(veryEasy_case)
            algorithm_chooser(veryEasy_case)

        if choose_default == "5":
            print("Doable selected" '\n')
            print_puzzle(doable_case)
            algorithm_chooser(doable_case)

        if choose_default == "6":
            print("Impossible selected" '\n')
            print_puzzle(impossible_case)
            algorithm_chooser(impossible_case)

    if choose_puzzle == "2":  # custom puzzle

        print("Enter your puzzle, use a zero to represent the blank." '\n')

        row_one = input("Enter the first row, use space between numbers." '\n')

        row_two = input(
            "Enter the second row, use space between numbers." '\n')

        row_three = input(
            "Enter the third row, use space between numbers." '\n')

        row_one = [int(i) for i in row_one.split(" ")]
        row_two = [int(i) for i in row_two.split(" ")]
        row_three = [int(i) for i in row_three.split(" ")]

        custom_puzzle = [row_one, row_two, row_three]

        print_puzzle(custom_puzzle)

        algorithm_chooser(custom_puzzle)


main()
