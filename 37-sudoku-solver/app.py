# 37. Sudoku Solver
# https://leetcode.com/problems/sudoku-solver/

from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(row: int, col: int, num: str) -> bool:
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False
            row_start, col_start = 3 * (row // 3), 3 * (col // 3)
            for i in range(row_start, row_start + 3):
                for j in range(col_start, col_start + 3):
                    if board[i][j] == num:
                        return False
            return True

        def backtrack() -> bool:
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for num in '123456789':
                            if is_valid(row, col, num):
                                board[row][col] = num
                                if backtrack():
                                    return True
                                board[row][col] = '.'
                        return False
            return True

        backtrack()