#!/usr/bin/python3
"""this module contains a program that solves the N queens problem
"""
import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at the specified position.

    Args:
        board (list): The current state of the chessboard.
        row (int): The row index to check.
        col (int): The column index to check.
        N (int): The size of the chessboard.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(N):
    """
    Solve the N Queens problem and return a list of solutions.

    Args:
        N (int): The size of the chessboard.

    Returns:
        list: A list of solutions, where each solution
        is a list of queen positions.
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    def solve(row):
        if row == N:
            solutions.append([[i, r.index(1)] for i, r in enumerate(board)])
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                solve(row + 1)
                board[row][col] = 0

    solve(0)
    return solutions


def main():
    """
    Entry point of the program.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
        solutions = solve_n_queens(N)
        for solution in solutions:
            print(solution)
    except ValueError:
        print("N must be a number")
        sys.exit(1)


if __name__ == "__main__":
    main()
