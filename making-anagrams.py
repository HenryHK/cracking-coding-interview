#!/usr/bin/python3
# Idea: use a map to count how many times a char appears, and remove the difference.

import string


def number_needed(a, b):
    result = 0
    a_dict = {}
    b_dict = {}
    for letter in string.ascii_lowercase:
        a_dict[letter] = 0
        b_dict[letter] = 0

    for letter in a:
        a_dict[letter] += 1
    for letter in b:
        b_dict[letter] += 1

    for letter in string.ascii_lowercase:
        result += abs(a_dict[letter]-b_dict[letter])
    return result


a = input().strip()
b = input().strip()

print(number_needed(a, b))
