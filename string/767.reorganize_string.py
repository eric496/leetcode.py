"""
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
If possible, output any possible result.  If not possible, return the empty string.

Example 1:
Input: S = "aab"
Output: "aba"

Example 2:
Input: S = "aaab"
Output: ""

Note:
S will consist of lowercase letters and have length in range [1, 500].
"""

# Solution 1: O(n^2) TC
from collections import Counter


class Solution:
    def reorganizeString(self, S: str) -> str:
        cnt = Counter(S)

        if len(S) == 1:
            return S
        elif len(cnt) == 1:
            return ""

        res = ""

        while 1:
            # Reorg completes when it's all zeros in the frequency table
            if not sum(cnt.values()):
                break
            top, second = cnt.most_common(2)
            # When there is only one character left
            if top[1] == 1 and not second[1]:
                res += top[0]
                break
            # When the most frequent character is the only one left and its number is greater than 1,
            # it is impossible to reorganize without repetition
            elif top[1] > 1 and not second[1]:
                return ""
            # Otherwise append the most two common characters and update the frequency table
            else:
                res += top[0]
                res += second[0]
                cnt[top[0]] -= 1
                cnt[second[0]] -= 1

        return res
