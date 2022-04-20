"""
Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        count_nums1 = self.counter(nums1)
        count_nums2 = self.counter(nums2)

        out_list = []

        for key, val in count_nums1.items():
            if key in count_nums2.keys():
                out_list.extend([key] * min(val, count_nums2[key]))

        return out_list


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

    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(sol.intersect(nums1, nums2))
    # print(nums1[1:3], nums1[1:3] == nums2)

    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(sol.intersect(nums1, nums2))
    # print(nums1[0:2], nums1[0:2] == nums2[0:2])