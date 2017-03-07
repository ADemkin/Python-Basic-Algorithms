# coding: utf-8
#
# python 3.6
#
# Бинарный поиск по памяти без подглядывания
#
# Anton Demkin, 2017
#


def mem_BinarySearch(item, list):
    if len(list) < 2:
        return list

    left_bound = 0
    right_bound = len(list)
    while left_bound < right_bound:
        middle = (left_bound + right_bound) // 2
        if list[middle] < item:
            left_bound = middle + 1
        if list[middle] > item:
            right_bound = middle - 1
        if list[middle] == item:
            return middle
            break
    return -1


intList = [1, 4, 6, 7, 18, 23, 28, 32, 34, 45, 46, 48, 52, 64, 65, 67, 68, 77, 81, 93, 99]
# index:   0, 1, 2, 3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20

print(mem_BinarySearch(64, intList))
