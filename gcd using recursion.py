def gcd(a,b,remainder=None):
    if remainder is None:
        remainder = 0
    if a % b == 0:
        return remainder
    elif a%b!=0:
        remainder = a%b
        return gcd(b,remainder,remainder)


print(gcd(9,6))