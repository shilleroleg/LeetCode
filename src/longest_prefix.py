"""
14. Longest Common Prefix
Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.



Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lower-case English letters.
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        intersect = strs[0]
        for single_s in strs[1:]:
            intersect = [let for let in single_s if let in intersect]
        return ''.join(intersect)


if __name__ == '__main__':
    sol = Solution()
    strs = ["flower", "flow", "flight"]
    print(sol.longestCommonPrefix(strs))

    strs = ["dog", "racecar", "car"]
    print(sol.longestCommonPrefix(strs))

    strs = ["cir", "car"]
    print(sol.longestCommonPrefix(strs))

