"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:
Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.

Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True

Note:
The string size will be in the range [1, 100].
"""


# Solution 1: brute force DFS
class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True
        
        return self.dfs(s, 0, 0)
        
    def dfs(self, s: str, i: int, cnt: int) -> bool:
        if cnt < 0:
            return False
        
        if i == len(s):
            return cnt == 0
        
        if s[i] == "(":
            return self.dfs(s, i+1, cnt+1)
        elif s[i] == ")":
            return self.dfs(s, i+1, cnt-1)
        elif s[i] == "*":
            return self.dfs(s, i+1, cnt+1) or self.dfs(s, i+1, cnt-1) or self.dfs(s, i+1, cnt)


# Solution 2: count the min and max possible numbers of left open brackets
class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open_left = max_open_left = 0
        
        for c in s:
            if c == "(":
                min_open_left += 1
                max_open_left += 1
            elif c == ")":
                min_open_left -= 1
                max_open_left -= 1
            elif c == "*":
                min_open_left -= 1
                max_open_left += 1
                
            if min_open_left < 0:
                min_open_left = 0
                
            if max_open_left < 0:
                return False
                        
        return min_open_left == 0
