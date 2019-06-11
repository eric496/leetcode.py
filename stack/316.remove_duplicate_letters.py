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
        stk, cnt, visited = [], [0]*26, [0]*26
        
        for ch in s:
            cnt[ord(ch)-ord('a')] += 1
            
        for ch in s:
            ix = ord(ch) - ord('a')
            cnt[ix] -= 1
            
            if not visited[ix]:
                while stk and ord(stk[-1]) > ord(ch) and cnt[ord(stk[-1])-ord('a')]:
                    visited[ord(stk[-1])-ord('a')] = 0
                    stk.pop()

                stk.append(ch)
                visited[ord(ch)-ord('a')] = 1
            
        return ''.join(stk)
