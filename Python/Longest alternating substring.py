"""Task
Given a string of digits, return the longest substring with alternating odd/even or even/odd digits. If two or more substrings have the same length, return the substring that occurs first.

Examples
longest_substring("225424272163254474441338664823") ➞ "272163254"
# substrings = 254, 272163254, 474, 41, 38, 23

longest_substring("594127169973391692147228678476") ➞ "16921472"
# substrings = 94127, 169, 16921472, 678, 476

longest_substring("721449827599186159274227324466") ➞ "7214"
# substrings = 7214, 498, 27, 18, 61, 9274, 27, 32
# 7214 and 9274 have same length, but 7214 occurs first.

longest_substring("20") ➞ "2"

longest_substring("") ➞ ""
Input Constraints
0 <= len(digits) <= 10^5
"""

previous = -1
def longest_substring(digits):
    number_dict = {0: 0, 1: 1, 2: 0, 3: 1, 4: 0, 5: 1, 6: 0, 7: 1, 8: 0, 9: 1}
    size_array = []
    count = 0
    global previous
    if len(digits) == 0:
        return ""
    else:
        for num in digits:
            if number_dict[int(num)] != previous:
                previous = number_dict[int(num)]
                count += 1
            else:
                count = 0
            size_array.append(count)
            print(num, number_dict[int(num)], count)
        largest_size = max(size_array)
        print(largest_size)
        print(size_array.index(largest_size) - largest_size,size_array.index(largest_size))
        print(digits[size_array.index(largest_size) - largest_size], digits[size_array.index(largest_size)])
    return "".join(digits[size_array.index(largest_size) - largest_size:size_array.index(largest_size)+1])

print(longest_substring("225424272163254474441338664823"))
print(longest_substring("721449827599186159274227324466"))
