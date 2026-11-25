"""
Given a string s of '(' , ')' and lowercase English characters. 
Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
Formally, a parentheses string is valid if and only if:
It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Example 4:
Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
 
Constraints:
1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.
"""


"""
Thought Process:
    1. Track unmatched parentheses by index: Only unmatched '(' and ')'
       need removal; lowercase letters always stay.
    2. Scan left-to-right with a stack:
       - On '(': Push its index onto `stack` (pending a future ')').
       - On ')': If `stack` is non-empty, pop the matching '(' index;
         otherwise, this ')' has no opener, so record its index in `to_remove`.
    3. Collect leftover openers: After the scan, any indices remaining in
       `stack` are unmatched '('—add them to `to_remove`.
    4. Rebuild the valid string: Join all characters whose index is not in
       `to_remove` in O(n) time.

Complexity:
    Time: O(n) — two linear passes over `s` with O(1) set lookups.
    Space: O(n) — for `stack`, `to_remove`, and the output character list.
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_remove = set()

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)

        to_remove.update(stack)

        return "".join(c for i, c in enumerate(s) if i not in to_remove)
