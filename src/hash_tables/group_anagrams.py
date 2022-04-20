"""
Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}

        for str1 in strs:
            str_sort = ''.join(sorted(str1))
            if str_sort in hash_table.keys():
                hash_table[str_sort].append(str1)
            else:
                hash_table[str_sort] = [str1]

        return [val for _, val in hash_table.items()]


if __name__ == "__main__":

    sol = Solution()

    strs = ["eat","tea","tan","ate","nat","bat"]
    print(sol.groupAnagrams(strs))                   # -> [["bat"],["nat","tan"],["ate","eat","tea"]]
