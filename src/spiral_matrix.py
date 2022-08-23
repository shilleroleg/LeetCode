"""
54. Spiral Matrix
Medium

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l_row = len(matrix[0])
        l_col = len(matrix)

        gorizont = 1
        vertical = 0

        visit = {(0, 0): 1}

        cur = [0, 0]
        out = [matrix[0][0]]
        n = 1

        while n < l_row*l_col:
            if gorizont == 1 and (cur[1] == l_row - 1 or (cur[0] + vertical, cur[1] + gorizont) in visit):
                gorizont = 0
                vertical = 1
            elif gorizont == -1 and (cur[1] == 0 or (cur[0] + vertical, cur[1] + gorizont) in visit):
                gorizont = 0
                vertical = -1
            elif vertical == 1 and (cur[0] == l_col - 1 or (cur[0] + vertical, cur[1] + gorizont) in visit):
                gorizont = -1
                vertical = 0
            elif vertical == -1 and (cur[0] == 0 or (cur[0] + vertical, cur[1] + gorizont) in visit):
                gorizont = 1
                vertical = 0

            cur = [cur[0] + vertical, cur[1] + gorizont]
            out.append(matrix[cur[0]][cur[1]])
            visit[(cur[0], cur[1])] = 1
            n += 1

        return out


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().spiralOrder(matrix))  # -> [1,2,3,6,9,8,7,4,5]

    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(Solution().spiralOrder(matrix))  # -> [1,2,3,4,8,12,11,10,9,5,6,7]

    matrix = [[3], [2]]
    print(Solution().spiralOrder(matrix))  # -> [1,2,3,6,9,8,7,4,5]