# coding: utf-8
#
# python 3.6
#
# This is a recursion algorithm for calculating a factorial of a given number
#
# Anton Demkin, 2017
#


def factorial(number):
    if number == 0:
        # we cannon return 0, but 1 will make nothing because x * 1 = x
        # how else can i make this line of code?
        # this part should return nothing, but should not break sequence
        return 1
    if number > 0:
        number = number * factorial(number - 1)
    return number


print(factorial(5))
