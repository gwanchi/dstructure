"""
Given a string str, create a function that returns all its possible subsequences, the order doesn't matter.
"""
def getSubsequences(str):
    subsequences = []
    def rec(str, i, subsequence):
        if i == len(str):
            subsequences.append(subsequence)
        else:
            rec(str, i+1, subsequence + str[i])
            rec(str, i+1, subsequence)
    rec(str, 0, "")
    return subsequences

string = "abcd"
print(getSubsequences(string))