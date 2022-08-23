"""
43. Multiply Strings
Medium

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2,
also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = self.s2i(num1) * self.s2i(num2)
        return self.i2s(ans)

    def i2s(self, int_: int) -> str:
        i2s_dict = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
        out_s = ''
        while int_ >= 10:
            ost = int_ % 10
            int_ //= 10
            out_s += i2s_dict[ost]
        out_s += i2s_dict[int_]
        return out_s[-1::-1]

    def s2i(self, str_: str) -> int:
        r_str = str_[-1::-1]
        s2i_dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        out_int = 0
        for ind, s in enumerate(r_str):
            out_int += s2i_dict[s] * 10**ind

        return out_int

if __name__ == '__main__':
    num1 = "123"
    num2 = "456"
    print(Solution().multiply(num1, num2))  #-> "56088"

    num1 = "140"
    num2 = "721"
    print(Solution().multiply(num1, num2))  # -> "4"


