# Sudoku Processor

Author: Jachym Svejda

This repository serves as a submission place for the [JEM207](https://is.cuni.cz/studium/predmety/index.php?do=predmet&kod=JEM207&skr=2023) final project. The project is centered around sudoku. It creates various sudoku problems and their solution. 

Presumably a user interested in solving sudoku will mostly use `solve_sudoku()` that can both solve given puzzle or reveal only one of the missing cells. Of course, you can use it to reveal one of the filled in cells as well, though it is not of much use.

We believe the notebook `generation.ipynb` in the `Sudoku puzzles` folder will guide you well throughout the project. You can also find a set of test cases used for `solve_sudoku()` function in the `test_solving_function.py` file.

The project is created as follows:

1. functions used to shuffle sudoku are created
2. functions used to verify and display sudoku are created
3. 'base sudoku' is defined and new sudokus are generated (all completely filled in)
4. function used to solve sudoku or given clues is created
5. sudoku problems (i.e. with missing numbers) is created
6. sudokus are graded and put together with the solved version, problem verison and the grading
7. the clues distribution is shown in a histogram and data are exported into a `.csv` file 
8. an exemplary use is presented.
