"""
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.
Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.
Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

Example 1:
Input: "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Example 2:
Input: "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

Example 3:
Input: "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".

Note:
S.length <= 10000
S[i] is "(" or ")"
S is a valid parentheses string
"""

"""
Thought process:
    Create a variable to count the number of open parentheses.
    Traverse the characters in the string, if the current is an open parenthesis 
    and count is greater than 0 (indicating it is an inner open parenthesis), 
    then push it to the result array. 
    if the current is a closing parenthesis and count is greater than 1 ((indicating it is an inner closing parenthesis)),
    then push it to the result array.
    At each iteration, update the count variable accordingly.
"""

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res, openp = [], 0
        
        for ch in S:
            if ch == '(' and openp > 0:
                res.append(ch)
            elif ch == ')' and openp > 1:
                res.append(ch)
                
            openp += 1 if ch == '(' else -1
            
        return ''.join(res)
