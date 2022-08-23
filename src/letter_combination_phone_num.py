from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        lend = len(digits)

        if lend == 0:
            return []

        list_let = [phone[d] for d in digits]

        first = list_let[0]

        for second in range(1, lend):
            temp = []
            for f in first:
                for s in list_let[second]:
                    temp.append(f+s)
            first = temp

        return first


if __name__ == '__main__':
    digits = "23"
    print(Solution().letterCombinations(digits))  #-> ["ad","ae","af","bd","be","bf","cd","ce","cf"]

