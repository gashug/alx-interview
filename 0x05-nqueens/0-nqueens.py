#!/usr/bin/env python3
import sys

def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].
    This means checking the column and both diagonals for any existing queens.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(n, row=0, board=[], solutions=[]):
    """
    Recursively solve the N Queens problem using backtracking.
    
    Args:
    - n: The size of the board (n x n) and the number of queens.
    - row: The current row to place a queen.
    - board: The current state of the board.
    - solutions: A list to store all the valid solutions.
    
    Returns:
    - A list of all valid solutions, where each solution is represented
      as a list of [row, column] pairs.
    """
    if row == n:
        solution = []
        for r, c in enumerate(board):
            solution.append([r, c])
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board.append(col)
            solve_n_queens(n, row + 1, board, solutions)
            board.pop()

    return solutions

def main():
    # Handle command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    # Solve the N Queens problem
    solutions = solve_n_queens(N)

    # Print each solution
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
