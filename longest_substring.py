"""
Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        letters = {}
        tail = 0
        head = 0
        result = 0
        while head < len(s):
            # print("%d - %d" % (head, tail))
            # print(letters)
            # print("===========================")
            if s[head] in letters:
                tail = max(tail, letters[s[head]])
            letters[s[head]] = head
            result = max(result, head - tail)
            head += 1
        return result


print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))

