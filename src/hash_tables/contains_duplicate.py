"""
Contains Duplicate II

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array
such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count_nums = self.counter(nums)

        non_uniqs = [k for k, v in count_nums.items() if v > 1]

        for nu in non_uniqs:
            firsti, *otheri = [i for i, j in enumerate(nums) if j == nu]
            for i in otheri:
                if abs(firsti - i) <= k:
                    return True
                else:
                    firsti = i
        return False


    def counter(self, nums: List[int]) -> dict:
        mapper = {}
        for num in nums:
            if num in mapper.keys():
                mapper[num] += 1
            else:
                mapper[num] = 1
        return mapper


if __name__ == "__main__":

    sol = Solution()

    nums = [1,2,3,1]
    k = 3
    print(sol.containsNearbyDuplicate(nums, k))     # -> True

    nums = [1, 0, 1, 1]
    k = 1
    print(sol.containsNearbyDuplicate(nums, k))  # -> True

    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    print(sol.containsNearbyDuplicate(nums, k))     # -> False