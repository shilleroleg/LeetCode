from typing import List, Set, Tuple


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sums = set()
        for ind, n in enumerate(nums):
            sum2 = self.twoSum(nums[ind+1:], -1*n)
            for s in sum2:
                sums.add(tuple(sorted((n, s[0], s[1]))))
        return sums


    def twoSum(self, nums: List[int], target: int) -> Set[Tuple[int, ...]]:
        hash_map = {}  # val: ind
        out = set()
        for ind, num in enumerate(nums):
            if target - num in hash_map:
                out.add(tuple(sorted((nums[hash_map[target - num]], num))))
                hash_map[num] = ind
            else:
                hash_map[num] = ind

        return out


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums))  #-> [[-1,-1,2],[-1,0,1]]

    nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
    print(Solution().threeSum(nums))  # -> [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
