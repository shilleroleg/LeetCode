"""Merge sorted lists by inserting"""

from typing import List


class Solution:
    def insert_sort(self, *iterable) -> List[int]:

        out = []

        for it in iterable:
            out = self._merge(out, it)

        return out

    def _merge(self, first: List[int], second: List[int]):
        if len(first) == 0:
            return second
        if len(second) == 0:
            return first

        outs = []
        u1, u2 = 0, 0

        while u1 < len(first) and u2 < len(second):
            if first[u1] < second[u2]:
                outs.append(first[u1])
                u1 += 1
            else:
                outs.append(second[u2])
                u2 += 1
        outs.extend(first[u1:])
        outs.extend(second[u2:])
        return outs


if __name__ == '__main__':
    b = [1, 2, 3, 5, 7]
    a = [2, 4, 6]
    c = [6, 7, 9, 11, 13]

    print(Solution().insert_sort(a, b, c))  #
