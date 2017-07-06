# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]

incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]

incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]


# Navigate through column and return true if same element is found in the column

def element_in_Column(sudoku, element, p1, p2, length):
    x = 0
    y = p2
    cleng = length
    for k in sudoku:
        #        print sudoku [x][y]
        bol = sudoku[x][y] == element
        if bol:
            if x == p1:
                bol = False
        cleng -= 1
        x += 1
        if bol:
            return True
    return False


# Navigate through the row and return true if same element is found in the row

def element_in_row(sudoku, element, p1, p2, length):
    x = p1
    y = 0
    cleng = length
    for k in sudoku:
        #        print sudoku [x][y]
        bol = sudoku[x][y] == element
        if bol:
            if y == p2:
                bol = False
        cleng -= 1
        y += 1
        if bol:
            return True
    return False


# checking for each element in sudoku if that element exits only once in the row and column
def check_sudoku(sudoku):
    p1 = 0
    p2 = 0
    length = len(sudoku)
    for k in sudoku:

        for element in k:
            # checking if the element is in the range 1 to n
            if element in range(1, length + 1):
                col = element_in_Column(sudoku, element, p1, p2, length)
                row = element_in_row(sudoku, element, p1, p2, length)
                if col == False:
                    if row == False:
                        p2 += 1
                        if p2 == length:
                            p2 = 0
                else:
                    return False
            else:
                return False
        p1 += 1
        if p1 == length:
            return True


print (check_sudoku(incorrect))
# >>> False

# print check_sudoku(correct)
# >>> True

# print check_sudoku(incorrect2)
# >>> False

# print check_sudoku(incorrect3)
# >>> False

# print check_sudoku(incorrect4)
# >>> False

# print check_sudoku(incorrect5)
# >>> False


