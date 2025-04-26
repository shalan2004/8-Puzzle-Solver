# 8-Puzzle-Solver
An AI-based 8-Puzzle Solver developed in Python using the Greedy Best-First Search algorithm.

Course: Artificial Intelligence — 3rd Year, Computer Science Department
Supervised by: Dr. Sara El-Metwally and Eng. Habiba Mohamed

Team Contributors:
- Abdulrahman Shalan
- Saleh Mostafa
- Noura Elsaey

# Project Overview
The 8-Puzzle is a classic AI problem where the goal is to arrange tiles numbered 0–8 into the correct order.
Our program allows users to input any 3×3 matrix and automatically solves it using Greedy Best-First Search guided by Manhattan Distance.

# Features
- Accepts user-defined 3×3 puzzle input.
- Checks if the puzzle is solvable.
- Solves using Greedy Best-First Search (Manhattan heuristic).
- Displays the steps towards the goal state.
- Handles unsolvable cases.

# Repository Contents
1. [README.md]: (https://github.com/shalan2004/8-Puzzle-Solver/blob/main/README.md): Overview and details about the project.
2. [Presentation.pdf]: (https://drive.google.com/file/d/1WPO-eSwMY4m0u80zrxoi5jKcb-dMoSGu/view?usp=sharing): The project presentation.
3. [game.py]: (https://github.com/shalan2004/8-Puzzle-Solver/blob/main/game.py): The Python code for the game.

# Note:
0 represents the empty tile.
The solver checks for inversions to ensure the puzzle is solvable before proceeding.
