"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

class Solution:
    def isValid(self, s: str):

        Flag = True
        pars = {'{': '}', '[': ']', '(': ')', '}': '{', ']': '[', ')': '('}

        if (len(s) % 2 != 0):
            return False

        for i in range(len(s) - 1):
            if (s[i] in pars and (s[i + 1] != pars[s[i]] and s[i - 1] != pars[s[i]]  and pars[s[i]] != s[len(s) - i - 1])):
                Flag = False

        return Flag


    def isValid2(self, s):
        stack = [] # create an empty stack to store opening brackets
        for c in s: # loop through each character in the string
            if c in '([{': # if the character is an opening bracket
                stack.append(c) # push it onto the stack
            else: # if the character is a closing bracket
                if not stack or \
                    (c == ')' and stack[-1] != '(') or \
                    (c == '}' and stack[-1] != '{') or \
                    (c == ']' and stack[-1] != '['):
                    return False # the string is not valid, so return false
                stack.pop() # otherwise, pop the opening bracket from the stack
        return not stack # if the stack is empty, all opening brackets have been matched with their corresponding closing brackets,
                         # so the string is valid, otherwise, there are unmatched opening brackets, so return false



s = Solution()
print(s.isValid('('))
print(s.isValid('()[]{}'))
print(s.isValid('(]'))
print(s.isValid('{[]}'))
print(s.isValid('){'))
