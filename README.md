# Sudoku Processor

Author: Jachym Svejda

This repository serves as a submission place for the [JEM207](https://is.cuni.cz/studium/predmety/index.php?do=predmet&kod=JEM207&skr=2023) final project. The project is centered around sudoku. It creates various sudoku problems and their solution. 

Presumably a user interested in solving sudoku will be most interested in function `solve_sudoku()` that can both solve given puzzle or reveal only one of the missing cells. Of course, you can use it to reveal one of the filled in cells as well, though it is not of much use.

We believe the notebook `generation.ipynb` in the `Sudoku puzzles` folder will guide you well throughout the project.

The project is created as follows:

1. sudoku excersises are generated
2. a function is created to solved the excersises, give you hints and assign it a level of difficulty
3. testcases are used to test  performance of the function
4. the excersises are solved and a difficulty is assigned to it
