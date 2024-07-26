#!/usr/bin/env python3

from typing import Any


class SudokuSolution(object):
    # def isValidSudoku(self, board: list[list[Any]]) -> bool:
    #     """
    #     should iterate over the entire board, and check for
    #     repeated elements on rows, columns and squares

    #     approach:
    #       1 - check rows, and columns
    #       2 - check squares
    #           approach 2.1: get/create squares, and check on then
    #               pros: Readability
    #               cons: Memory and time complexity by creating new arrays
    #           approach 2.2: calculate new indexes for each square by
    #                         normalizing indexes.
    #     """
    #     for i in range(9):
    #         for j in range(9):
    #             if board[i][j] != "." and self._isRepeated(board, i, j):
    #                 return False
    #     return True

    def isValidSudoku(self, board: list[list[Any]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] != "." and self._isRepeated(board, i, j):
                    return False
        return True

    def _isRepeated(self, board: list[list[Any]], row: int, col: int) -> bool:
        for i in range(9):
            # checking row
            if board[row][i] == board[row][col] and i != col:
                return True

            # checking column
            if board[i][col] == board[row][col] and i != row:
                return True

        # checking squares by normalizing row and col to as square indexes
        sqrRow = (row // 3) * 3
        sqrCol = (col // 3) * 3
        for i in range(sqrRow, sqrRow + 3):
            for j in range(sqrCol, sqrCol + 3):
                if i != row and j != col and board[i][j] == board[row][col]:
                    return True
        return False
