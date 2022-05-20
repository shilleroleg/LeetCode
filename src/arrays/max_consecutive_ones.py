"""
Max Consecutive Ones

Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""
import unittest

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zeros_index = [-1]
        zeros_index.extend([i for i, num in enumerate(nums) if num == 0])
        zeros_index.append(len(nums))

        return max([y - x - 1 for (x, y) in zip(zeros_index[:-1], zeros_index[1:])])


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_search(self):
        nums = [1, 1, 0, 1, 1, 1]
        target = 3
        self.assertEqual(self.sol.findMaxConsecutiveOnes(nums), target)

    def test_search2(self):
        nums = [1, 0, 1, 1, 0, 1]
        target = 2
        self.assertEqual(self.sol.findMaxConsecutiveOnes(nums), target)


if __name__ == "__main__":
    unittest.main()

