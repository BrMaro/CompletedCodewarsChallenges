"""DESCRIPTION:
Complete the function/method so that it takes a PascalCase string and returns the string in snake_case notation. Lowercase characters can be numbers. If the method gets a number as input, it should return a string.

Examples
"TestController"  -->  "test_controller"
"MoviesAndBooks"  -->  "movies_and_books"
"App7Test"        -->  "app7_test"
1                 -->  "1"
STRINGS ALGORITHMS"""


def to_underscore(string):
    if type(string) == int:
        return (str(string))
    else:
        stringarr = []
        letterpos = []
        for j in string:
            stringarr.append(j)
        for i in range(len(stringarr)):
            if stringarr[i].isupper() == True and i != 0:
                letterpos.append(i)

        for i in range(len(letterpos)):
            stringarr.insert(letterpos[i] + i, "_")
        stringarr = ''.join(stringarr)
        return stringarr.lower()