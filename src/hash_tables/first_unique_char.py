"""
First Unique Character in a String

Solution
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.


Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1


Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:

        hashtable = {}
        max_index = len(s) + 1

        for n, key in enumerate(s):
            if key in hashtable.keys():
                hashtable[key] = n + max_index
            else:
                hashtable[key] = n

        return min(hashtable.values()) if min(hashtable.values()) < max_index else -1


if __name__ == "__main__":

    sol = Solution()

    s = "loveleetcode"
    print(sol.firstUniqChar(s))

    s = "aabb"
    print(sol.firstUniqChar(s))