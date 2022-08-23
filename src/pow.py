"""
50. Pow(x, n)
Medium

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104
"""

import math

class Solution:
    def myPow_naive(self, x: float, n: int) -> float:
        out = 1
        for _ in range(abs(n)):
            out *= x
        return out if n >=0 else 1/out

    def myPow(self, x: float, n: int) -> float:
        if x == 0.0:
            return 0.0
        ans = math.exp(n * math.log(abs(x), math.e))

        return -1*ans if (x < 0 and n%2 == 1) else ans


if __name__ == '__main__':
    x = 2.00000
    n = 10
    print(Solution().myPow(x, n))  #-> 1024.00000

    x = 2.00000
    n = -2
    print(Solution().myPow(x, n))  # -> 0.25000

    x = -2.00000
    n = 2
    print(Solution().myPow(x, n))  # -> 4

    x = 0.00001
    n = 2147483647
    print(Solution().myPow(x, n))  # ->