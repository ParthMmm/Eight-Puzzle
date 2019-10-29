

def main():

    choosePuzzle = input(
        "Welcome to Parth Mangrola's 8-puzzle solver. Type 1 to use a default puzzle, or 2 to enter your own puzzle." '\n')
    
    if choosePuzzle == "1":  # default puzzle
        print("default selected")

    if choosePuzzle == "2":  # custom puzzle
        print("Enter your puzzle,use a zero to represent the blank. " '\n'
              "Enter the first row, use space or tabs between numbers." '\n'
              "Enter the second row, use space or tabs between numbers." '\n'
              "Enter the third row, use space or tabs between numbers." '\n')
    return

main()
