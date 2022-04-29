from typing import List


def quick_sort(unsorted: List[int]) -> List[int]:
    if len(unsorted) < 2:
        return unsorted
    else:
        pivot = unsorted[0]
        less = [i for i in unsorted[1:] if i <= pivot]
        greater = [i for i in unsorted[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    uns_list = [5, 4, 3, 2, 1]

    print(quick_sort(uns_list))

    uns_list = [1, 2, 3, 4, 5]

    print(quick_sort(uns_list))

    uns_list = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]

    print(quick_sort(uns_list))