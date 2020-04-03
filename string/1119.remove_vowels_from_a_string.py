"""
Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

Example 1:
Input: "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"

Example 2:
Input: "aeiou"
Output: ""

Note:
S consists of lowercase English letters only.
1 <= S.length <= 1000
"""


class Solution:
    def removeVowels(self, S: str) -> str:
        res = []

        for ch in S:
            if ch not in "aeiou":
                res.append(ch)

        return "".join(res)
