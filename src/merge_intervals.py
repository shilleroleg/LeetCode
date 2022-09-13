"""
56. Merge Intervals
Medium

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:

    1 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 104
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        cursor = intervals[0]
        out = []

        for i in range(1, len(intervals)):
            current = intervals[i]
            if cursor[1] >= current[0]:
                cursor = [min(cursor[0], current[0]), max(cursor[1], current[1])]
            else:
                out.append(cursor)
                cursor = current
        out.append(cursor)
        return out


if __name__ == '__main__':
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(Solution().merge(intervals))  # -> [[1,6],[8,10],[15,18]]

    intervals = [[1,4], [0,4]]
    print(Solution().merge(intervals))  # -> [[0, 4]]

    intervals = [[1,4], [0,0]]
    print(Solution().merge(intervals))  # -> [[0,0],[1,4]]

    intervals = [[1,4],[1,4]]
    print(Solution().merge(intervals))  # -> [[1,4]]

    intervals = [[1,4],[0,1]]
    print(Solution().merge(intervals))  # -> [[0,4]]

