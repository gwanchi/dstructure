"""
Given a string str made of alphabetical letters only, create a function that returns the length of the longest palindrome string that can be made from letters of str
"""
def longest_palindrome(str):
    occurrences=[0]*128
    for letter in str:
        occurrences[ord(letter)] += 1
    length=0
    for occu in occurrences:
        length += occu if occu % 2 == 0 else occu - 1
    if length < len(str):
        length += 1
    return length