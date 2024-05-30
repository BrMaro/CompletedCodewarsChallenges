"""
LINK:https://www.codewars.com/kata/5aec1ed7de4c7f3517000079/train/python

Your task is to write a function that does just what the title suggests (so, fair warning, be aware that you are not getting out of it just throwing a lame bas sorting method there) with an array/list/vector of integers and the expected number n of smallest elements to return.

Also:

the number of elements to be returned cannot be higher than the array/list/vector length;
elements can be duplicated;
in case of duplicates, just return them according to the original order (see third example for more clarity).
Same examples and more in the test cases:

first_n_smallest([1,2,3,4,5],3) == [1,2,3]
first_n_smallest([5,4,3,2,1],3) == [3,2,1]
first_n_smallest([1,2,3,4,1],3) == [1,2,1]
first_n_smallest([1,2,3,-4,0],3) == [1,-4,0]
first_n_smallest([1,2,3,4,5],0) == []
Performance version by FArekkusu also available.

ARRAYS LISTS  DATA STRUCTURES ALGORITHMS

"""
def first_n_smallest(arr, n):
    sumlist = sum(arr[:n])
    smallest = sumlist
    for i in range(n, len(arr)):
        sumlist+=arr[i]
        sumlist -= arr[i-n]
    if sumlist < smallest:
        smallest = sumlist
    return smallest

print(first_n_smallest())