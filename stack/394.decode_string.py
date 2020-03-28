"""
Given an encoded string, return it's decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stk, rep, cur = [], 0, ''
        
        for c in s:
            if c.isdigit():
                rep = rep*10 + int(c)
            elif c.isalpha():
                cur += c
            elif c == '[':
                stk.append(cur)
                stk.append(rep)
                rep = 0
                cur = ''
            elif c == ']':
                n = stk.pop()
                prev = stk.pop()
                cur = prev + n*cur
        
        return cur
                