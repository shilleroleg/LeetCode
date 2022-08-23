"""
15. 3Sum
Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[1] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

    3 <= nums.length <= 3000
    -105 <= nums[i] <= 105
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sums = []
        for ind, n in enumerate(nums):
            sum2 = self.twoSum(nums, -1*n, ind)
            if sum2 is not None:
                sums.append([n, nums[sum2[0]], nums[sum2[1]]])
        print(sums)
        set_sums = []
        need_sums = []
        for s in sums:
            if set(s) not in set_sums:
                set_sums.append(set(s))
                need_sums.append(s)

        return need_sums

    def twoSum(self, nums2: List[int], target: int, stop_ind: int) -> List[int]:
        hash_map = {}  # val: ind
        for ind, num in enumerate(nums2):
            if ind == stop_ind:
                continue
            if target - num in hash_map:
                return [hash_map[target - num], ind]
            else:
                hash_map[num] = ind


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums))  # -> [[-1,-1,2], [-1,0,1]]

    nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    print(Solution().threeSum(nums))  # -> [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
    # no [-3,-1,4],[-3,0,3],[-2,-1,3]
