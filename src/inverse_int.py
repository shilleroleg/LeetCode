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

        neg = -1 if x < 0 else 1
        ans = 0
        x = abs(x)

        while x > 0:
            div, mod = divmod(x, 10)
            ans = ans*10 + mod
            x = div

        ans *= neg
        if pow(-2, 31) < ans < pow(2, 31) - 1:
            return ans
        else:
            return 0


if __name__ == '__main__':
    n = -123
    print(Solution().reverse(n))  #-> 321
