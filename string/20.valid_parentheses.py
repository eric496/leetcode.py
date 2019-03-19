'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''

'''
Thought:
    Use a map with closing/right parenthesis as keys and open/left parenthesis as values. Use a stack to store the characters in the input string. 
    Loop through the characters in the input string, each character is either a open or closing parenthsis only. 
    If it is an open parenthesis, then simply add it to the stack. 
    If it is a closing parenthesis, then pop the top element in the stack and pair it with the closing parenthesis. Return false if they cannot form a pair. 
    
    If the current character is a closing parenthesis, always check if the stack is empty, 
    because we cannot pop items from an empty stack and the current closing parenthesis has nothing to form a pair. It should directly return false.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        pairs = {'(':')', '{':'}', '[':']'}
        for ch in s:
            if ch in pairs:
                stk.append(pairs[ch])
            elif not stk or stk.pop() != ch:
                return False
        return stk == []
