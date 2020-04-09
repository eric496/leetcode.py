"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:
1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.

Follow up:
Can you solve it in O(N) time and O(1) space?
"""


# Solution: two stacks - O(n) TC, O(n) SC
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stk1, stk2 = [], []

        for c in S:
            if c.isalpha():
                stk1.append(c)
            elif c == "#":
                if stk1:
                    stk1.pop()

        for c in T:
            if c.isalpha():
                stk2.append(c)
            elif c == "#":
                if stk2:
                    stk2.pop()

        return stk1 == stk2


# Follow up - two pointers
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:        
        i = len(S) - 1
        j = len(T) - 1
        skips_S = skips_T = 0
        
        while i >= 0 or j >= 0:
            while i >= 0 and (S[i] == "#" or skips_S):
                if S[i] == "#":
                    skips_S += 1
                else:
                    skips_S -= 1
                
                i -= 1
            
            while j >= 0 and (T[j] == "#" or skips_T):
                if T[j] == "#":
                    skips_T += 1
                else:
                    skips_T -= 1
                
                j -= 1
            
            if S[i] != T[j]:
                return False
        
            i -= 1
            j -= 1
        
        return True
