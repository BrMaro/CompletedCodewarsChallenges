# https://www.codewars.com/kata/55c6126177c9441a570000cc/train/python

def lexicographic_value(s):
    value = 0
    max_length = 15
    padded_s = s.ljust(max_length, '0')
    for i,char in enumerate(padded_s):
        value += (10**(len(padded_s) - i - 1) * int(char))+len(s)
    return value

print(lexicographic_value("10003"),lexicographic_value("22"))
def ordering(n):
    sum = 0
    for i in n:
        sum += int(i)
    return sum * 10**10 + lexicographic_value(n)


# print(sorted(["2000", "11", "11"]))


def order_weight(strng):
    return ' '.join(sorted(strng.split(), key=ordering))


print(order_weight('21 130 4 50 132 51 43 170 44 71 162 144 117 55 64 70120 182 38 183 157 116401 85 176 176 291020 95 177 177 33802 24056 198 206470 421192 137640 20289 330259 450706 411673 107745 321990 149065 454624 140498 165941 126855 255492 96156 317828 77834 259835 407995'))