"""
38. Count and Say
Medium

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a
different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring
contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally,
concatenate every said digit.

For example, the saying and conversion for digit string "3322251":

Given a positive integer n, return the nth term of the count-and-say sequence.

Example 1:

Input: n = 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        out = '1'
        for i in range(2, n+1):
            out = self.compress(out)
        return out

    def compress(self, i_str: str) -> str:
        current = i_str[0]
        count = 0
        o_str = ''
        for i in i_str:
            if i == current:
                count += 1
            else:
                o_str += str(count) + str(current)
                current = i
                count = 1

        return o_str + str(count) + str(current)


if __name__ == '__main__':
    n = 1
    print(Solution().countAndSay(n))  #-> "1"

    n = 4
    print(Solution().countAndSay(n))  # -> "1211"

    n = 10
    print(Solution().countAndSay(n))  # -> "13211311123113112211"