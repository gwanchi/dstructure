"""
Given a string str made of 3 types of brackets only (){}[], create a function that checks if the string is valid. The string is considered as valid if all opening brackets are closed with the same type of brackets, and in the correct order.
"""
def isValid(str):
    bracketsMap = {'(':')','{':'}','[':']'}
    openingBrackets = ['(','{','[']
    stack = []
    for bracket in str:
        if bracket in openingBrackets:
            stack.append(bracket)
        elif len(stack) > 0 and bracket == bracketsMap[stack[-1]]:
            stack.pop()
        else:
            return False
    return len(stack) == 0