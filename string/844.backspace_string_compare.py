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

class Solution:
    def backspaceCompare(self, S:str, T:str) -> bool:
        s_stk, t_stk = [], []
        
        for ch in S:
            if ch == '#' and s_stk:
                s_stk.pop()
            elif ch != '#':
                s_stk.append(ch)
        
        for ch in T:
            if ch == '#' and t_stk:
                t_stk.pop()
            elif ch != '#':
                t_stk.append(ch)

        return s_stk == t_stk

# more straightforward solution
class Solution:
    def backspaceCompare(self, S:str, T:str) -> bool:
        s_stk, t_stk = [], []
        
        for ch in S:
            if ch != '#':
                s_stk.append(ch)
            else:
                if not s_stk:
                    continue
                else:
                    s_stk.pop()
        
        for ch in T:
            if ch != '#':
                t_stk.append(ch)
            else:
                if not t_stk:
                    continue
                else:
                    t_stk.pop()
                    
        return s_stk == t_stk