"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]

Note:
S will be a string with length between 1 and 12.
S will consist only of letters or digits.
"""


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if not S:
            return []

        res = []
        self.backtrack(list(S), res, 0)

        return res

    def backtrack(self, chars: str, res: List[str], pos: int) -> None:
        if pos == len(chars):
            res.append("".join(chars))
            return

        if chars[pos].isdigit():
            self.backtrack(chars, res, pos + 1)
            return
        else:
            chars[pos] = chars[pos].lower()
            self.backtrack(chars, res, pos + 1)

            chars[pos] = chars[pos].upper()
            self.backtrack(chars, res, pos + 1)
