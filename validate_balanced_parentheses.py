"""
Validate Balanced Parentheses

Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses in the program are balanced. Every opening bracket must have a corresponding closing bracket. We can approximate this using strings.

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.

Example:

Input: "((()))"
Output: True

Input: "[()]{}"
Output: True

Input: "({[)]"
Output: False

Solution:
This can be done using a stack. Iterating through the string one character at a time, whenever we see an opening bracket, we push it onto the stack. If we see a closing bracket, we check whether or not the character on the top of the stack is the corresponding type of opening bracket. If it is not, the string is invalid. When we have reached the end of the string, if the stack is not empty, there were more opening brackets than closing brackets and we know the string is invalid.

This algorithm runs in O(n) time. We iterate through the string s once and the append/pop operations on the stack are in constant O(1) time.
This algorithm uses linear space, O(n). In the worst case, such as for a string like "((({{[{[(" we will have no closing parentheses and will thus push all of the opening parentheses onto the stack.


"""
class Solution:
    def isValid(self,s):
        openParens = ['(', '{', '[']
        closingParens = [')', '}', ']']
        stack = []
        for char in s:
            # If we see a bracket that is part of the set
            # of possible opening options, put it on the stack.
            if char in openParens:
                stack.append(char)
            elif char in closingParens:
                # if the stack is empty, there is an extra
                # closing parenthesis and s is invalid
                if len(stack) <= 0:
                    return False
                # compares the closing parenthesis to the
                # corresponding opening parenthesis using
                # their matching indices. We could also use
                # a hash map for this.
                if openParens.index(stack.pop()) != closingParens.index(char):
                    return False
        # if the stack is empty, the paranthesis
        # were balanced and s is valid.
        return len(stack) == 0

# Test Program
s = "()(){(())"
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))