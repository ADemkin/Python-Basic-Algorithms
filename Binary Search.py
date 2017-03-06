# coding: utf-8
# python 3.6
#
# a simple binary search on a given list
#
# Anton Demkin, 2017
#


def binSearch(searchValue, inputList):
    ''' Makes a binary search on a given list. \n
    Returns an index of searched value or -1 if value is not found.
    Usage: binSearch(value, list)'''
    low_index = 0
    high_index = len(inputList) - 1

    while (low_index <= high_index):
        mid_index = (low_index + high_index) // 2
        # if found return index
        if inputList[mid_index] == searchValue:
            return mid_index
        # if item is in the right side of the list
        if inputList[mid_index] > searchValue:
            high_index = mid_index - 1
        # if item is in the left side of the list
        if inputList[mid_index] < searchValue:
            low_index = mid_index + 1

    # if nothing found return -1
    if low_index > high_index:
        return -1


testList = [1, 4, 6, 7, 18, 23, 28, 32, 34, 45, 46, 48, 52, 64, 65, 67, 68, 77, 81, 93, 99]
# index:    0, 1, 2, 3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20

print(binSearch(46, testList))

def test():
    # testing
    print(binSearch(18,testList) == 4)
    print(binSearch(99, testList) == 20)
    print(binSearch(34, testList) == 8)
    print(binSearch(5, [1,2,3,4,5,6,7,8,9]) == 4)
    print(binSearch(8, [1,2,3,4,5,6,7,8,9]) == 7)

# test()

# Python Basic Algorithms

