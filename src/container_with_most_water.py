"""
11. Container With Most Water
Medium

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints
of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water
(blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1


Constraints:

    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) - 1

        while right - left > 0:
            if height[left] < height[right]:
                res = max(res, height[left] * (right - left))
                left += 1
            else:
                res = max(res, height[right] * (right - left))
                right -= 1

        return res


        # for ind, h in enumerate(height):
        #     ends = length - 1
        #     while ends > ind:
        #         s.append(min(h, height[ends]) * (ends-ind))
        #         ends -= 1
        #
        # return max(s)


if __name__ == '__main__':
    height = [2, 3, 4, 5, 18, 17, 6]
    print(Solution().maxArea(height))  # -> 17

    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(Solution().maxArea(height))  # -> 49

    height = [1, 1]
    print(Solution().maxArea(height))  # -> 1

