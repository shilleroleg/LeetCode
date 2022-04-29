"""
4Sum II

Given four integer arrays nums1, nums2, nums3, and nums4 all of length n,
return the number of tuples (i, j, k, l) such that: 0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
Example 2:

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1

Constraints:

n == nums1.length
n == nums2.length
n == nums3.length
n == nums4.length
1 <= n <= 200
-228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228
"""
import time
from typing import List

# Декоратор для подсчета времени выполнения функции
def time_decorator(func):
    def _inner(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        work_time = time.time() - start
        work_time_min = work_time // 60
        work_time_sec = work_time % 60
        print(f'Working time = {work_time_min:.0f} min {work_time_sec:.3f} sec')
        return result

    return _inner



class Solution:
    def fourSumCount_bruteForce(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # TOO LONG

        n = len(nums1)
        count = 0
        for i1 in range(n):
            for i2 in range(n):
                for i3 in range(n):
                    for i4 in range(n):
                        if nums1[i1] + nums2[i2] + nums3[i3] + nums4[i4] == 0:
                            count += 1
        return count

    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        hash_map1 = self._twoSum(nums1, nums2)
        hash_map2 = self._twoSum(nums3, nums4)

        count = 0

        for key1, val1 in hash_map1.items():
            if hash_map2.get(-key1):
                count += val1 * hash_map2.get(-key1)

        return count

    def _twoSum(self, nums1: List[int], nums2: List[int]) -> dict:
        hash_map = {}
        for num1 in nums1:
            for num2 in nums2:
                if num1 + num2 in hash_map:
                    hash_map[num1 + num2] += 1
                else:
                    hash_map[num1 + num2] = 1
        return hash_map


if __name__ == "__main__":
    sol = Solution()

    start = time.time()
    nums1, nums2, nums3, nums4 = [1,2], [-2,-1], [-1,2], [0,2]
    print(sol.fourSumCount(nums1, nums2, nums3, nums4))                   # -> 2
    print(time.time() - start)

    start = time.time()
    nums1, nums2, nums3, nums4 = [0]*100, [0]*100, [0]*100, [0]*100
    print(sol.fourSumCount(nums1, nums2, nums3, nums4))
    print(time.time() - start)