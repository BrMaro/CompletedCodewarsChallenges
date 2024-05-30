"""
LINK:https://www.codewars.com/kata/65126a26597b8597d809de48/train/python

Given a number, insert duplicate digits on both sides of all digits which appear in a group of 1.

Worked Example
22733 ➞ 2277733

# The number can be split into groups 22, 7, and 33.
# 7 appears on its own.
# Put 7s on both sides to create 777.
# Put the numbers together and return the result.
Examples
123 ➞ 111222333

56657 ➞ 55566555777

33 ➞ 33
Notes
All tests will include positive integers.
"""

from itertools import groupby


def numbers_need_friends_too(num_string):
    num_list = [''.join(group) for _, group in groupby(str(num_string))]
    for i in range(len(num_list)):
        if len(num_list[i]) == 1:
            num_list[i] = num_list[i] * 3
    return int(''.join(num_list))


print(numbers_need_friends_too(12233456))
