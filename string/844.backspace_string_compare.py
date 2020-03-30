'''
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
'''


# Solution: two stacks - O(n) TC, O(n) SC
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stk1, stk2 = [], []
        
        for c in S:
            if c.isalpha():
                stk1.append(c)
            elif c == '#':
                if stk1:
                    stk1.pop()
        
        for c in T:
            if c.isalpha():
                stk2.append(c)
            elif c == '#':
                if stk2:
                    stk2.pop()
                    
        return stk1 == stk2


# Follow up
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_ptr = len(S) - 1
        t_ptr = len(T) - 1
        s_skips = t_skips = 0
        
        while s_ptr >= 0 or t_ptr >= 0: 
            while s_ptr >= 0:
                if S[s_ptr] == '#':
                    s_skips += 1
                    s_ptr -= 1
                elif s_skips > 0:
                    s_skips -= 1
                    s_ptr -= 1
                else:
                    break
                    
            while t_ptr >= 0:
                if T[t_ptr] == '#':
                    t_skips += 1
                    t_ptr -= 1
                elif t_skips > 0:
                    t_skips -= 1
                    t_ptr -= 1
                else:
                    break
                
            
            if s_ptr >= 0 and t_ptr >= 0 and S[s_ptr] != T[t_ptr]:
                return False
            
            if s_ptr >= 0 and t_ptr < 0 or t_ptr >= 0 and s_ptr < 0:
                return False
            
            s_ptr -= 1
            t_ptr -= 1
        
        return True
        