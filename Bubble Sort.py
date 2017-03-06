# coding: utf-8
#
# python 3.6
#
# My realisation of bubble sort algorithm
#
# Anton Demkin, 2017
#

def bubbleSort(inputList):
    '''This is one of simplest sorting algorithms, also one of the slowest.
    It requires a list on input and returns a new list.
    Usage: bubbleSort(list)'''

    # check if list is long enough
    if len(inputList) < 2:
        return inputList

    # create variable for highest unsorted index
    high_index = len(inputList)
    # if sorted length is less than list length, then sort
    while high_index > 1:
        # walk through array elements one by one
        for i in range(0, high_index - 1):
            # if current element is greater than next one, swap them
            if inputList[i] > inputList[i + 1]:
                # swap
                [inputList[i], inputList[i + 1]] = [inputList[i + 1], inputList[i]]
        # every cycle in bubble sort largest list member is always on the top
        # than mean that N from largest number will be on top in N moves
        # that means that we do not need to check indexes > N in a new passes
        high_index -= 1
    # return list
    return inputList


listToSort = [8, 35, 14, 28, 15, 13, 26, 22, 32, 3, 18, 19, 33, 12, 21, 34, 29, 1, 7, 5, 2, 20, 25, 6, 27, 16, 31, 9,
              36, 23, 11, 30, 24, 4, 17, 10]
# print(listToSort)
print(bubbleSort(listToSort))
