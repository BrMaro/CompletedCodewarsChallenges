# https://www.codewars.com/kata/55aa075506463dac6600010d/train/python

def divisor_square_sum(n):
    square_sum = 0
    for factor in range(1, int(n ** 0.5) + 1):
        if n % factor == 0:
            square_sum += factor ** 2 + (n//factor) ** 2 if n//factor != factor else factor ** 2
    return square_sum

def list_squared(m, n):
    result = []
    for i in range(m, n + 1):
        if int(divisor_square_sum(i) ** 0.5) ** 2 == divisor_square_sum(i):
            result.append([i, divisor_square_sum(i)])
    return result


print(list_squared(1, 250))
