"""
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.
Formally, a parentheses string is valid if and only if:
It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

Example 1:
Input: "())"
Output: 1

Example 2:
Input: "((("
Output: 3

Example 3:
Input: "()"
Output: 0

Example 4:
Input: "()))(("
Output: 4

Note:
S.length <= 1000
S only consists of '(' and ')' characters.
"""


"""
Thought Process:
    1. Cancel matched pairs on the fly: Maintain `stack` holding unmatched
       parentheses seen so far.
    2. Scan left-to-right across `s`:
       - When seeing ')': Check if `stack` is non-empty and its top is '('.
         If so, pop '(' because this pair is valid and cancels out.
         Otherwise, push ')' onto `stack` as an unmatched closer.
       - When seeing '(': Push '(' onto `stack` as an unmatched opener.
    3. Count leftovers: Every remaining '(' in `stack` needs a ')' inserted,
       and every remaining ')' needs a '(' inserted, so return `len(stack)`.

Complexity:
    Time: O(n) — single linear scan over `s`; each character is pushed and
          popped at most once.
    Space: O(n) — worst-case stack size when no pairs match (e.g., "(((").
"""


# Solution 1: stack - O(n) TC and O(n) SC
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for c in s:
            if c == "(":
                stack.append(c)
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(c)
        
        return len(stack)


"""
Thought Process:
    1. Define the two kinds of missing parentheses:
       - `need_close`: Number of ')' needed to close currently unclosed '('
         characters seen so far (acts like the size of an open-bracket stack).
       - `need_open`: Number of '(' needed to balance stray ')' characters
         that appeared when no unclosed '(' was available (`need_close == 0`).
    2. Scan left-to-right across `s`:
       - When seeing '(': It requires a future ')', so increment `need_close += 1`.
       - When seeing ')':
         * If `need_close > 0`, pair it with the most recent unclosed '(' by
           decrementing `need_close -= 1`.
         * Otherwise (`need_close == 0`), this ')' can never be matched by a
           later '(', so increment `need_open += 1` to insert a '(' before it.
    3. Combine both insertion counts: After scanning all characters, every
       remaining unclosed '(' still needs a ')' (`need_close`), and every stray
       ')' needed a '(' (`need_open`), so return `need_open + need_close`.

Complexity:
    Time: O(n) — single linear scan through the string of length n.
    Space: O(1) — only two integer counters are maintained.
"""


# Solution 2: count needed brackets - O(n) TC and O(1) SC
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        need_open = 0
        need_close = 0

        for c in s:
            if c == "(":
                need_close += 1
            else:  # c == ")"
                if need_close > 0:
                    need_close -= 1
                else:
                    need_open += 1

        return need_open + need_close
