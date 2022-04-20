"""
Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

Example 1:

Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8.
Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:

    board.length == 9
    board[i].length == 9
    board[i][j] is a digit 1-9 or '.'.
"""
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res_line = self.check_line(board)
        if not res_line:
            return False
        # Transpose
        t_board = list(map(list, zip(*board)))
        res_col = self.check_line(t_board)
        if not res_col:
            return False
        #
        res_square = self.check_square(board)
        if not res_square:
            return False

        return True

    def check_line(self, board: List[List[str]]) -> bool:
        for line in board:
            hash_table = set()
            for el in line:
                if el in hash_table and el != '.':
                    return False
                else:
                    hash_table.add(el)
        return True

    def check_square(self, board: List[List[str]]) -> bool:

        b_square = [set() for _ in range(9)]

        for str1 in range(9):
            for col in range(9):
                val = board[str1][col]
                idx = (str1 // 3) * 3 + col // 3
                if val in b_square[idx] and val != '.':
                    return False
                b_square[idx].add(val)

        return True


if __name__ == "__main__":
    sol = Solution()

    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(sol.isValidSudoku(board))                         # -> True

    board = [[".",".",".",".","5",".",".","1","."]
        ,[".","4",".","3",".",".",".",".","."]
        ,[".",".",".",".",".","3",".",".","1"]
        ,["8",".",".",".",".",".",".","2","."]
        ,[".",".","2",".","7",".",".",".","."]
        ,[".","1","5",".",".",".",".",".","."]
        ,[".",".",".",".",".","2",".",".","."]
        ,[".","2",".","9",".",".",".",".","."]
        ,[".",".","4",".",".",".",".",".","."]]
    print(sol.isValidSudoku(board))                            # -> False
