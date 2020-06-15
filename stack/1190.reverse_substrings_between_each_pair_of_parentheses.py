"""
You are given a string s that consists of lower case English letters and brackets. 
Reverse the strings in each pair of matching parentheses, starting from the innermost one.
Your result should not contain any brackets.

Example 1:
Input: s = "(abcd)"
Output: "dcba"

Example 2:
Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.

Example 3:
Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.

Example 4:
Input: s = "a(bcdefghijkl(mno)p)q"
Output: "apmnolkjihgfedcbq"

Constraints:
0 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It's guaranteed that all parentheses are balanced.
"""


# Solution 1: Brute force - O(n^2) TC and O(n) SC
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = []

        for c in s:
            if c == ")":
                rev = []

                while stk and stk[-1] != "(":
                    rev.append(stk.pop())

                if stk and stk[-1] == "(":
                    stk.pop()

                stk += rev
            else:
                stk.append(c)

        return "".join(stk)


# Solution 2: O(n) TC and O(n) SC
