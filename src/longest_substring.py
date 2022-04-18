"""
3. Longest Substring Without Repeating Characters
Medium

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        start = 0
        max_len = 1
        hash_map = {}   #val: ind
        # Sliding window from start to stop
        while start < len(s):
            for stop, subs in enumerate(s[start:], start):
                if subs not in hash_map:
                    hash_map[subs] = stop
                else:
                    max_len = max(max_len, stop - start)
                    start += 1      # Move window
                    hash_map = {}   # Clear hash map
                    break
                if stop == len(s)-1:
                    max_len = max(max_len, stop - start + 1)
        return max_len


if __name__ == '__main__':
    sol = Solution()
    s = "abcabcbb"
    print(sol.lengthOfLongestSubstring(s))      # -> 3

    s = "au"
    print(sol.lengthOfLongestSubstring(s))      # -> 2


