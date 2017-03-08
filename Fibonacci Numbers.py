# coding: utf-8
#
# python 3.6
#
# My version of fibonacci numbers calculator
#
# Anton Demkin, 2017
#

def fibonacci(number):
    '''Calculates fibonacci sequence from 0 to N, where N is index.
    Usage: fibonacci(N)'''
    sequence = [0, 1]

    if number == 0:
        return [0]
    if number == 1:
        return [0, 1]
    if number > 1:
        next = 0
        for j in range(1, number):
            next = sequence[j] + sequence[j - 1]
            sequence.append(next)
    return sequence


print(fibonacci(21))
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
# next sequence prints a golden ratio value calculated from two close members of fibonacci sequence.
# f = fibonacci(50)
# for i in range(1,len(f)-1):
#     print(f[i+1]/f[i])
