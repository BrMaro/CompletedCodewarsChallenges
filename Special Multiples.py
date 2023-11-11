"""
LINK:https://www.codewars.com/kata/55e785dfcb59864f200000d9/train/python

Some numbers have the property to be divisible by 2 and 3. Other smaller subset of numbers have the property to be divisible by 2, 3 and 5. Another subset with less abundant numbers may be divisible by 2, 3, 5 and 7. These numbers have something in common: their prime factors are contiguous primes.

Implement a function that finds the amount of numbers that have the first N primes as factors below a given limit.

Let's see some cases:

count_specMult(3, 200)  =>  6

The first 3 primes are: 2, 3 and 5.

And the found numbers below 200 are: 30, 60, 90, 120, 150, 180.
Happy coding!!
MATHEMATICS ALGORITHMS
"""


def isprime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_product_of_n_consecutive_primes(n):
    primelist = [2]
    product = 2
    number = 3
    while len(primelist) < n:
        if isprime(number):
            primelist.append(number)
            product *= number
        number += 1
    return product


def count_specMult(n,max_val):
    return max_val//get_product_of_n_consecutive_primes(n)



print(count_specMult(3,200))
