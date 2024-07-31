from collections import Counter

def scramble(s1, s2):
    count_s1 = Counter(s1)
    count_s2 = Counter(s2)
    for char in count_s2:
        if count_s2[char] > count_s1.get(char, 0):
            return False
    return True

