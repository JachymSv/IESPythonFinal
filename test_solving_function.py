import unittest
import numpy as np
import random


# define a function (copied from generation.ipynb) to be tested

# check if num can be place at board[row][col]
def is_valid(board, row, col, num):
    # check the row
    if num in board[row, :]:
        return False
    # check the column
    if num in board[:, col]:
        return False
    # check the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    if num in board[start_row:start_row + 3, start_col:start_col + 3]:
        return False
    return True

# backtracking function to solve the Sudoku.
def backtrack(board, solutions):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # find an empty cell
                for num in range(1, 10):  # try all possible numbers
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        backtrack(board, solutions)
                        if len(solutions) > 1:  # stop if two solutions are found
                            return
                        board[row][col] = 0  # reset cell for backtracking
                return
    # if we complete the board, save the solution
    solutions.append(''.join(str(num) for num in board.flatten()))
    if len(solutions) > 1:  # stop if two solutions are found
        return

# solve the Sudoku problem
def solve_sudoku(board_str, coords=[]):
    # convert the input string to a 9x9 matrix
    board = np.array([int(char) for char in board_str]).reshape(9, 9)

    # to store solutions
    solutions = []

    # start solving
    backtrack(board, solutions)
    
    # return the solutions as a numpy array
    if coords == []:
        return np.array(solutions)
    
    # if coords are specified, return error if there are multiple or no solutions
    elif len(solutions) == 0:
        return "ERROR: Sudoku problem is not solvable. Please provide a valid problem."
    elif len(solutions) == 2:
        return "ERROR: Sudoku problem has multiple solutions. Please provide a problem with a unique solution."
    
    # if coords are specified and only 1 solution exists, return input with filled in coords
    row_keys={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8}
    
    for i in range(len(coords)):
        j = row_keys[coords[i][0]]*9 + int(coords[i][1])-1
        board_str = [char for char in board_str]
        board_str[j] = [char for char in solutions[0]][j]
    
    return ''.join(char for char in board_str)


# Test cases for the `solve_sudoku` function

class test_solve_function(unittest.TestCase):
    
    def test_add_one_clue(self):
        self.assertEqual(solve_sudoku('000014090104003050073950400005739604006000073030405020400100230389020701501340908', ['A1']), '600014090104003050073950400005739604006000073030405020400100230389020701501340908')
        
    def test_add_multiple_clues(self):
        self.assertEqual(solve_sudoku('000014090104003050073950400005739604006000073030405020400100230389020701501340908', ['A1','A3']), '602014090104003050073950400005739604006000073030405020400100230389020701501340908')
        
    def test_solve_whole_sudoku(self):
        self.assertEqual(solve_sudoku('000014090104003050073950400005739604006000073030405020400100230389020701501340908'), '652814397194673852873952416215739684946281573738465129467198235389526741521347968')

if __name__ == '__main__':
    unittest.main()