"""DESCRIPTION:
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

Examples (input --> output):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"
ALGORITHMS"""


def dec2hex(n):
    rem = ""
    if n == 0:
        rem = rem + str(0) + str(0)
    else:
        while n > 0:
            if n % 16 == 10:
                rem = rem + "A"
            elif n % 16 == 11:
                rem = rem + "B"
            elif n % 16 == 12:
                rem = rem + "C"
            elif n % 16 == 13:
                rem = rem + "D"
            elif n % 16 == 14:
                rem = rem + "E"
            elif n % 16 == 15:
                rem = rem + "F"
            elif n % 16 < 10:
                rem = rem + (str(n % 16))
            else:
                rem = rem + (str(n % 16))
            n = n // 16
    if len(rem) < 2:
        rem = rem + "0"
    return rem[::-1]


# print(dec2hex(275))
def rgb(r, g, b):
    if r < 0:
        r = 0
    elif r > 255:
        r = 255
    else:
        pass
    if g < 0:
        g = 0
    elif g > 255:
        g = 255
    else:
        pass
    if b < 0:
        b = 0
    elif b > 255:
        b = 255
    else:
        pass

    return dec2hex(r) + dec2hex(g) + dec2hex(b)