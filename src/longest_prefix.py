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
        # Find words with smallest length
        min_len = min([len(st) for st in strs])
        intersect = [st for st in strs if len(st) == min_len][0]
        #
        for single_s in strs:
            i = 1
            # Run by window
            while i <= len(single_s):
                if single_s[0:i] in intersect[0:i]:
                    i += 1
                else:
                    intersect = intersect[0:i-1]
                    break
        return intersect


if __name__ == '__main__':
    sol = Solution()
    strs = ["flower", "flow", "flight"]     # 'fl'
    print(sol.longestCommonPrefix(strs))

    strs = ["dog", "racecar", "car"]        # ''
    print(sol.longestCommonPrefix(strs))

    strs = ["cir", "car"]                   # 'c'
    print(sol.longestCommonPrefix(strs))

    strs = ["ab", "a"]                      # 'a'
    print(sol.longestCommonPrefix(strs))

    strs = ["reflower", "flow", "flight"]   # ''
    print(sol.longestCommonPrefix(strs))

    strs = ["a", "b"]                       # ''
    print(sol.longestCommonPrefix(strs))

    strs = ["aa", "ab"]                     # 'a'
    print(sol.longestCommonPrefix(strs))




