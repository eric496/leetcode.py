"""
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:
Input: "bcabc"
Output: "abc"

Example 2:
Input: "cbacdcbc"
Output: "acdb"
"""

"""
Thoguht process:
    Traverse the string, use a stack to store characters. 
    Whenever the current character is smaller than the previous one, 
    check if all characters before the current one has duplicate coming after the current one. 
    If there is, then remove the one before. Push the current character into the stack.

    Use an array to count the frequencies of all characters.
    Use an array to store all visited characters so to skip duplicates.
"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_i = {c: i for i, c in enumerate(s)}
        stk = []
        visited = set()
        
        for i, c in enumerate(s):
            if c in visited:
                continue
                
            while stk and c < stk[-1] and last_i[stk[-1]] > i:
                visited.remove(stk.pop())
                
            stk.append(c)
            visited.add(c)
            
        return "".join(stk)
