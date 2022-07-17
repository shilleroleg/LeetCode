"""
7. Reverse Integer
Medium

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside
the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

Constraints:

    -231 <= x <= 231 - 1
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x > 2**31 - 1 or x < -2**31:
            return 0
        strx = str(x)
        if x >= 0:
            out = int(strx[-1::-1])
        else:
            out = int('-' + strx[-1:0:-1])

        if out > 2**31 - 1 or out < -2**31:
            out = 0

        return out



if __name__ == '__main__':
    x = -123
    print(Solution().reverse(x))  # -> 321

    x = 1534236469
    print(Solution().reverse(x))  # -> 0


