"""
47. Permutations II
Medium

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
from itertools import permutations
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return {p for p in permutations(nums)}


if __name__ == '__main__':
    nums = [1,2,3]
    print(Solution().permuteUnique(nums))  #-> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    nums = [1, 1, 2]
    print(Solution().permuteUnique(nums))  # -> [[1,1,2], [1,2,1], [2,1,1]]
