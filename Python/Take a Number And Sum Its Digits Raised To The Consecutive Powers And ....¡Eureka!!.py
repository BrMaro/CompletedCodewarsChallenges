"""refer:https://www.codewars.com/kata/5626b561280a42ecc50000d1/solutions/python"""


def separateDigits(num):
    a = []
    num = str(num)
    for j in num:
        a.append(int(j))
    return a


def raiseIncreasingPowers(arr):
    powarr = []
    resultarr = []
    for v in range(len(arr)):
        powarr.append(v + 1)
        resultarr.append(arr[v] ** powarr[v])
    return resultarr


def sum_dig_pow(a, b):
    ans = []
    for i in range(a, b + 1):
        if i == sum(raiseIncreasingPowers(separateDigits(i))):
            ans.append(i)
    return (ans)