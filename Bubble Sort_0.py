# coding: utf-8
#
# python 3.6
#
# Пузырьковая сортировка, практика по памяти без подглядывания
#
# Anton Demkin, 2017
#

intList = [8, 35, 14, 28, 15, 13, 26, 32, 3, 18, 19, 35, 12, 21, 34, 29, 1, 7, 5]
strList = ['g', 'f', 'd', 'b', 'c', 'e', 'a']


def mem_BubbleSort(list):
    if len(list) < 2:
        return list
    sorted = False
    sorted_index = len(list) - 1
    sorted_length = 0
    while not sorted:
        for i in range(0, sorted_index):
            if list[i + 1] < list[i]:
                [list[i], list[i + 1]] = [list[i + 1], list[i]]
                sorted_length = 0
            if list[i + 1] > list[i]:
                sorted_length += 1
            if sorted_length == len(list) - 1:
                sorted = True
    return list


print(mem_BubbleSort(intList))
print(mem_BubbleSort(strList))
