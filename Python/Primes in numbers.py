
# def is_prime(n):
#     if n == 2 or n == 3: return True
#     if n < 2 or n % 2 == 0: return False
#     if n < 9: return True
#     if n % 3 == 0: return False
#     r = int(n ** 0.5)
#     f = 5
#     while f <= r:
#         if n % f == 0: return False
#         if n % (f + 2) == 0: return False
#         f += 6
#     return True
#
#
# def p_factors(n):
#     factor = []
#     for i in range(2, n + 1):
#         if n % i == 0 and is_prime(i):
#             factor.append(i)
#     return factor
#
# print(p_factors(10))


def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if is_prime[p] == True:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n + 1) if is_prime[p]]
    return prime_numbers


# def p_factors(n):
#     prime_list = sieve_of_eratosthenes(n)
#     p_factors = []
#     for i in prime_list:
#         if n % i == 0:
#             p_factors.append(i)
#     return p_factors
#
#
# def prime_factors(n):
#     pf = p_factors(n)
#     print(pf)
#     powers = []
#     string = ""
#     for i in pf:
#         count = 0
#         while n % i == 0:
#             n = n / i
#             count += 1
#         powers.append(count)
#     for i in range(len(pf)):
#         if powers[i] == 1:
#             string = string + "(" + str(pf[i]) + ")"
#         else:
#             string = string + "(" + str(pf[i]) + "**" + str(powers[i]) + ")"
#     return string


def prime_factors(n):
    prime_list = sieve_of_eratosthenes(int(n ** 0.5) + 1)
    pf = []
    powers = []
    original_n = n

    for prime in prime_list:
        if prime * prime > n:
            break
        if n % prime == 0:
            count = 0
            while n % prime == 0:
                n //= prime
                count += 1
            pf.append(prime)
            powers.append(count)

    if n > 1:
        pf.append(n)
        powers.append(1)

    result = ""
    for i in range(len(pf)):
        if powers[i] == 1:
            result += f"({pf[i]})"
        else:
            result += f"({pf[i]}**{powers[i]})"

    return result

print(prime_factors(3000))
