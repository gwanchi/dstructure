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

    # Best Solution
    def longestSubstringWithoutRepeating(self, str):
        maxLength=0
        start=0
        indexes=[-1]*128
        for i in range(len(str)):
            if indexes[ord(str[i])] >= start:
                start=indexes[ord(str[i])]+1
            indexes[ord(str[i])]=i
            maxLength=max(maxLength, i-start+1)
        return maxLength


print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))

