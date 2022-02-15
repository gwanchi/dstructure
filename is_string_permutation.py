"""
Determine if a string is a permutation of another string.
"""
from collections import Counter


def is_permutation(str1, str2):
    for i in str1:
        if i not in str2:
            return False
    return True


print(is_permutation('dog', 'doggo'))
