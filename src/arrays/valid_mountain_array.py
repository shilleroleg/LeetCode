"""
Valid Mountain Array

Solution
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
"""


class Solution(object):
    def validMountainArray(self, arr):
        """
        Solution from LeetCode
        :type arr: List[int]
        :rtype: bool
        """
        len_arr = len(arr)
        counter = 0
        if len_arr < 3:
            return False

        # Walk up
        while counter + 1 < len_arr and arr[counter] < arr[counter + 1]:
            counter += 1

        if counter == 0 or counter == len_arr - 1:
            return False

        # Walk down
        while counter + 1 < len_arr and arr[counter] > arr[counter + 1]:
            counter += 1

        return counter == len_arr - 1


if __name__ == '__main__':
    sol = Solution()
    arr = [0, 3, 2, 1]
    print(sol.validMountainArray(arr))  # -> True

    arr = [2, 0, 2]
    print(sol.validMountainArray(arr))  # -> False

    arr = [0, 1, 2, 1, 2]
    print(sol.validMountainArray(arr))  # -> False
