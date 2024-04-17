# Artificial-Intelligence - 26 - Puzzle Problem
# Project Description: 
Implement the A* search algorithm with graph search (no repeated states) for solving the 26-puzzle problem as described below.  Use h(n)= Sum of Manhattan distances of the tiles from their goal positions as heuristic function. Your program will read in the initial and goal states from an input file and then generate an output file that contains the solution.  

# The 26-puzzle problem: 
The game board consists of three 3 x 3 grids stacked together. There are 26 tiles, numbered 1 to 26, and a blank position. A tile can move into the blank position if it is adjacent to the blank position in the x, y or z directions.  We can define six virtual moves (actions) for the blank position: East (E), West (W), North 
(N), South (S), Up (U) and Down (D). Given an initial state, the goal is to find a move sequence with a minimum number of moves to reach a given goal state. For example, the optimal solution for the initial and goal states is ESDWDNW.

![image](https://github.com/AnuOscar2308/Artificial-Intelligence/assets/83712797/30e8aaf0-4eb7-43b4-ab57-932a862da7fc)


# Input and output files: 
Your program will read in the values for the initial state and goal state from a text file that contains 23 lines. Lines 1 to 11 contain the tile patterns for the three layers of the initial state, with the layers separated by blank lines. Line 12 is a blank line. Lines 13 to 23 contain the three layers of the goal state, with the layers separated by blank lines. n and m are integers that range from 0 to 26, representing the blank position (0) and the tile numbers (1-26.)  Your program will produce an output file that contains 28 lines. Lines 1 to 23 contain the tile patterns for the initial state and goal state. You can simply copy lines 1 to 23 from the input file to the output file. Line 24 is a blank line. Line 25 is the depth level d of the shallowest goal node as found by the A* algorithm (assume the root node is at level 0.) Line 26 is the total number of nodes N generated in your tree (including the root node.) Line 27 contains the solution (a sequence of actions from root node to goal node) represented by A’s. The A’s are separated by blank spaces.  Each A is a character from the set {E, W, N, S, U, D}, representing the East, West, North, South, Up and Down movements of the blank position. Line 28 contains the f(n) values of the nodes along the solution path, from the root node to the goal node, separated by blank spaces. There should be d number of A values in line 27 and d+1 number of f values in line 28. 

![image](https://github.com/AnuOscar2308/Artificial-Intelligence/assets/83712797/cd01d052-109e-48c0-9d55-3403ac7e4b84)
