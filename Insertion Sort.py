# coding: utf-8
#
# python 3.6
#
# My realisation of insertion sort algorythm
#
# Anton Demkin, 2017
#


def insertionSort(inputList):
    '''My realisation of insertion sort
    Usage: insertionSort(list)'''

    # check for length of input
    if len(inputList) < 2:
        return inputList

    # index on the right side
    # also used to stop search
    # and swap elements
    rightBorderIndex = len(inputList) - 1
    # index of element with highest value
    highestValueIndex = None
    # value of element with highest value
    highestValue = 0

    while rightBorderIndex > 0:
        # find highest value and store its index in highestValueIndex variable
        for j in range(0, rightBorderIndex):
            if inputList[j] > highestValue:
                highestValue = inputList[j]
                highestValueIndex = j
        # swap value in right side of unsorted list and highest value found
        [inputList[highestValueIndex], inputList[rightBorderIndex]] = [inputList[rightBorderIndex],
                                                                       inputList[highestValueIndex]]
        # reduce search range by one and consider that part as sorted
        rightBorderIndex -= 1
        # reset highestValue
        highestValue = 0

    return inputList


# end function


listToSort = [8, 35, 14, 28, 15, 13, 26, 22, 32, 3, 18, 19, 33, 12, 21, 34, 29, 1, 7, 5, 2, 20, 25, 6, 27, 16, 31, 9,
              36, 23, 11, 30, 24, 4, 17, 10]

shortListToSort = [3, 1, 5, 4, 2]
# index            0, 1, 2, 3, 4
print(insertionSort(listToSort))
