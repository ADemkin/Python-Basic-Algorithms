# coding: utf-8
#
# python 3.6
#
# Prime numbers calculator
#
# Anton Demkin, 2017
#

def primeNumber(number):
    '''Calculates a list of prime numbers.
    Usage: primeNumber(N), where N is last member of list.'''
    prime_numbers = []
    for n in range(1, number + 1):
        divisions = 0
        for i in range(1, n + 1):
            # 5/5 == 5//5 -> true
            # 5/4 == 5//4 -> false
            if (n / i == n // i):
                divisions += 1
        if divisions == 2:
            prime_numbers.append(i)
    return prime_numbers


print(primeNumber(50))
