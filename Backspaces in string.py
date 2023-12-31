"""DESCRIPTION:
Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"

Your task is to process a string with "#" symbols.

Examples
"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  ""
FUNDAMENTALSSTRINGSALGORITHMS"""


def clean_string(s):
    arr = []
    s = list(s)
    for i in s:
        if i == "#" and len(arr) > 0:
            arr.pop()
        else:
            if i != "#":
                arr.append(i)
    return ''.join(arr)
