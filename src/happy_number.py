"""
Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:

Input: n = 2
Output: false

Constraints:

    1 <= n <= 231 - 1
"""
from typing import List


class Solution:
    def isHappy(self, n: int) -> bool:
        list_n = self._get_list(n)
        hash_map = set()
        while True:
            temp = self._sum_square(list_n)
            print(temp)
            if temp == 1:
                return True
            else:
                if temp in hash_map:
                    return False
                else:
                    hash_map.add(temp)
                    list_n = self._get_list(temp)

    @staticmethod
    def _sum_square(list_num):
        return sum([n*n for n in list_num])

    @staticmethod
    def _get_list(num: int) -> List[int]:
        return [int(n) for n in list(str(num))]


if __name__ == "__main__":

    obj = Solution()

    num = 19
    print(obj.isHappy(num))

    num = 2
    print(obj.isHappy(num))