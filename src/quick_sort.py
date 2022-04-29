from typing import List
import random


def quick_sort(unsorted: List[int]) -> List[int]:
    len_list = len(unsorted)
    if len_list < 2:
        return unsorted
    else:
        pivot_index = random.randint(0, len_list - 1)
        pivot = unsorted[pivot_index]

        less = [i for n, i in enumerate(unsorted) if i <= pivot and n != pivot_index]
        greater = [i for n, i in enumerate(unsorted) if i > pivot and n != pivot_index]

        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    uns_list = [5, 4, 3, 2, 1]

    print(quick_sort(uns_list))

    uns_list = [1, 2, 3, 4, 5]

    print(quick_sort(uns_list))

    uns_list = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]

    print(quick_sort(uns_list))