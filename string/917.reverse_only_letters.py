'''
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

Example 1:
Input: "ab-cd"
Output: "dc-ba"

Example 2:
Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:
Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
 
Note:
S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S doesn't contain \ or "
'''

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        start, end = 0, len(S)-1
        sl = list(S)
        
        while start < end:
            while start < end and not S[start].isalpha():
                start += 1
            while start < end and not S[end].isalpha():
                end -= 1
            sl[start], sl[end] = sl[end], sl[start]
            start += 1
            end -= 1
        
        return ''.join(sl)
