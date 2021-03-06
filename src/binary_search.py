"""
704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:

    1 <= nums.length <= 104
    -104 < nums[i], target < 104
    All the integers in nums are unique.
    nums is sorted in ascending order.
"""
from typing import List
import unittest


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        stop = len(nums)
        count = 0
        while count < len(nums):
            mid = start + (stop - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                stop = mid
                count += 1
                continue
            else:
                start = mid
                count += 1
                continue
        return -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_search_exists(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 9
        self.assertEqual(self.sol.search(nums, target), 4)

    def test_search_not_exists(self):
        nums = [-1, 0, 3, 5, 9, 12, 14]
        target = 2
        self.assertEqual(self.sol.search(nums, target), -1)


if __name__ == "__main__":
    unittest.main()
