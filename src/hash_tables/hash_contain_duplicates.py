from typing import List


class Solution:
    def containsDuplicate2(self, nums: List[int]) -> bool:
        hash_map = {}

        for num in nums:
            if num in hash_map.keys():
                return True
            else:
                hash_map[num] = 1

        return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)

        return False


if __name__ == "__main__":

    sol = Solution()

    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(sol.containsDuplicate(nums))

    nums = [1, 2, 3, 4]
    print(sol.containsDuplicate(nums))
