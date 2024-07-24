# https://www.codewars.com/kata/5547cc7dcad755e480000004/train/python

# def remov_nb(n):
#     sum_to_n = n*(n+1)/2
#     result = []
#     for i in range(n):
#         for j in range(i+1,n):
#             if (i*j + i+j) == sum_to_n:
#                 result.append((i,j))
#                 result.append((j,i))
#                 break
#     return result


def remov_nb(n):
    sum_to_n = n * (n + 1) // 2
    result = []
    for a in range(1, n + 1):
        b = (sum_to_n - a) / (a + 1)
        if b.is_integer() and 1 <= b <= n:
            result.append((a, int(b)))

    return result

print(remov_nb(101))