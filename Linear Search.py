# coding: utf-8
#
# python 3.6
#
# very simple linear search algorythm
#
# Anton Demkin, 2017
#

def linearSearch(searchValue, inputList):
    ''' A simplie linear search. Returns a number of element in list given or returns -1 if nothing found.
    Usage: linearSearch(value, list)'''
    index = 0
    for element in inputList:
        # increase index for every array element
        index += 1
        # if element is index, return index value
        if element == searchValue:
            return index
        # if index is last array element, then return -1
        if index == len(inputList):
            return -1


testList = [1, 4, 6, 7, 18, 23, 28, 32, 34, 45, 46, 48, 52, 64, 65, 67, 68, 77, 81, 93, 99]
# index:    0, 1, 2, 3, 4, 5, 6, 7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21


print(linearSearch(99, testList))
