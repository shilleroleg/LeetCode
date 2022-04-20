"""
Minimum Index Sum of Two Lists

Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.



Example 1:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".

Example 2:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).



Constraints:

    1 <= list1.length, list2.length <= 1000
    1 <= list1[i].length, list2[i].length <= 30
    list1[i] and list2[i] consist of spaces ' ' and English letters.
    All the stings of list1 are unique.
    All the stings of list2 are unique.
"""
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map_count = {}
        map_index = {}

        for n1, el1 in enumerate(list1):
            map_count[el1] = 1
            map_index[el1] = n1

        for n1, el1 in enumerate(list2):
            if el1 in map_count.keys():
                map_count[el1] += 1
            else:
                map_count[el1] = 1
            if el1 in map_index.keys():
                map_index[el1] += n1
            else:
                map_index[el1] = n1

        counts_2 = [key for key in map_count.keys() if map_count[key] > 1]
        min_index = min([map_index[key] for key in map_index.keys() if key in counts_2])
        return [key for key in map_index.keys() if key in counts_2 and map_index[key] == min_index]


if __name__ == "__main__":

    obj = Solution()

    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["KFC", "Shogun", "Burger King"]
    print(obj.findRestaurant(list1, list2))         # -> ["Shogun"]