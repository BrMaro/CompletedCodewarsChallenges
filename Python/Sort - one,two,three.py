"""DESCRIPTION:
Hey You !
Sort these integers for me ...

By name ...

Do it now !

Input
Range is 0-999

There may be duplicates

The array may be empty

Example
Input: 1, 2, 3, 4
Equivalent names: "one", "two", "three", "four"
Sorted by name: "four", "one", "three", "two"
Output: 4, 1, 3, 2
Notes
Don't pack words together:
e.g. 99 may be "ninety nine" or "ninety-nine"; but not "ninetynine"
e.g 101 may be "one hundred one" or "one hundred and one"; but not "onehundredone"
Don't fret about formatting rules, because if rules are consistently applied it has no effect anyway:
e.g. "one hundred one", "one hundred two"; is same order as "one hundred and one", "one hundred and two"
e.g. "ninety eight", "ninety nine"; is same order as "ninety-eight", "ninety-nine"""

def number_to_words(n):
    # Define lists of words for units, tens, and hundreds
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    # Helper function to convert a number less than 100 into words
    def convert_less_than_hundred(num):
        if num == 0:
            return ""
        elif num == 10:
            return "ten"
        elif num < 10:
            return units[num]
        elif num < 20:
            return teens[num - 10]
        else:
            return tens[num // 10] + " " + units[num % 10]

    # Check if the number is 0
    if n == 0:
        return "zero"

    # Convert the number into words for hundreds, tens, and units
    words = ""
    if n >= 100:
        words += units[n // 100] + " hundred"
        if n % 100 != 0:
            words += " and "

    words += convert_less_than_hundred(n % 100)

    return words


def sort_by_name(arr):
    arr = [(num, number_to_words(num)) for num in arr]
    sorted_tuples = sorted(arr, key=lambda x: x[1])
    return [num[0] for num in sorted_tuples]


print(sort_by_name([1, 2, 3, 4]))
