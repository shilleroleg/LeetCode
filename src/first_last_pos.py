"""
34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position
of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        stop = len(nums)-1

        out = [-1, -1]

        while stop >= start:
            if nums[start] == target:
                out[0] = start
            else:
                start += 1

            if nums[stop] == target:
                out[1] = stop
            else:
                stop -= 1

            if -1 not in out:
                return out

        return out




if __name__ == '__main__':
    nums = [5,7,7,8,8,10]
    target = 8
    print(Solution().searchRange(nums, target))  #-> [3,4]

    nums = [5,7,7,8,8,10]
    target = 6
    print(Solution().searchRange(nums, target))  # -> [-1, -1]

    nums = []
    target = 0
    print(Solution().searchRange(nums, target))  # -> [-1, -1]
