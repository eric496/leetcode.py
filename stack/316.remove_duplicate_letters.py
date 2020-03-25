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
        cnt = [0] * 26
        anchor = ord('a')
        
        for c in s:
            cnt[ord(c)-anchor] += 1
            
        stk = []
        visited = [0] * 26
        
        for c in s:
            cnt[ord(c)-anchor] -= 1
            
            if not visited[ord(c)-anchor]:
                while stk and ord(c) < ord(stk[-1]) and cnt[ord(stk[-1])-anchor]:
                    prev_letter = stk.pop()
                    visited[ord(prev_letter)-anchor] = 0

                stk.append(c)
                visited[ord(c)-anchor] = 1
            
        return ''.join(stk)
