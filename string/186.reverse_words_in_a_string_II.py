"""
Given an input string , reverse the string word by word. 

Example:
Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

Note: 
A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.

Follow up: Could you do it in-place without allocating extra space?
"""

"""
Thought process:
    Reverse each word and then reverse the whole list.
"""

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        start = 0

        for end in range(len(s)):
            if s[end] == ' ':
                self.reverse(s, start, end-1)
                start = end + 1
        
        # Reverse the last word which is not handled in the for-loop
        self.reverse(s, start, len(s)-1)
        # Reverse the whole list
        self.reverse(s, 0, len(s)-1)
        
        
    def reverse(self, s: List[str], low: int, high: int) -> None:
        while low < high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1
        