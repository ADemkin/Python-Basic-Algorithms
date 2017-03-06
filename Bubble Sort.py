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

    # create a variable to track progress
    sortedIndex = 0

    # if sorted length is less than list length, then sort
    while sortedIndex < len(inputList):
        # walk through array elements one by one
        for i in range(0, len(inputList) - 1):
            # if current element is greater than next one, swap them
            if inputList[i] > inputList[i + 1]:
                [inputList[i], inputList[i + 1]] = [inputList[i + 1], inputList[i]]
                sortedIndex = 0
            # if current element is less than next one, increase sorted index by 1
            if inputList[i] < inputList[i + 1]:
                sortedIndex += 1
    # return list
    return inputList



listToSort = [8, 35, 14, 28, 15, 13, 26, 32, 3, 18, 19, 35, 12, 21, 34, 29, 1, 7, 5]

print(bubbleSort(listToSort))
