"""
29. Divide Two Integers

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be
truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer
range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1,
and if the quotient is strictly less than -231, then return -231.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.

Constraints:

-231 <= dividend, divisor <= 231 - 1
divisor != 0
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        ans = 0
        pos = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        for i in range(31, -1, -1):
            if divisor << i <= dividend:
                dividend -= divisor << i
                ans += 1 << i

        out = ans if pos else -1*ans

        if out > 2**31-1:
            return 2**31-1
        elif out < -2**31:
            return -2**31
        else:
            return out


if __name__ == '__main__':
    dividend = 10
    divisor = 3
    print(Solution().divide(dividend, divisor))  #-> 3

    dividend = 7
    divisor = -3
    print(Solution().divide(dividend, divisor))  # -> -2

    dividend = -1
    divisor = -1
    print(Solution().divide(dividend, divisor))  # -> 1

    dividend = -2147483648
    divisor = -1
    print(Solution().divide(dividend, divisor))  # -> 2147483647


