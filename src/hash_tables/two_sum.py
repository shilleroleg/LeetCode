"""
1. Two Sum
Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]



Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""
from typing import List


class Solution:
    def twoSum_brutForce(self, nums: List[int], target: int) -> List[int]:
        # brut force
        for ind1, num1 in enumerate(nums):
            for ind2, num2 in enumerate(nums[ind1+1:], ind1+1):
                if num1 + num2 == target:
                    return [ind1, ind2]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}  # val: ind
        for ind, num in enumerate(nums):
            if target - num in hash_map:
                return [hash_map[target - num], ind]
            else:
                hash_map[num] = ind


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(sol.twoSum(nums, target))

    nums = [3,2,4]
    target = 6
    print(sol.twoSum(nums, target))

    nums = [0,4,3,0]
    target = 0
    print(sol.twoSum(nums, target))