"""
You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible non-empty sequences of letters you can make.

Example 1:
Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Example 2:
Input: "AAABBC"
Output: 188

Note:
1 <= tiles.length <= 7
tiles consists of uppercase English letters.
"""


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cnt = [0] * 26

        for ch in tiles:
            cnt[ord(ch) - ord("A")] += 1

        return self.backtrack(cnt)

    def backtrack(self, cnt: List[int]) -> int:
        sum_ = 0

        for i in range(26):
            if cnt[i]:
                sum_ += 1
                cnt[i] -= 1
                sum_ += self.backtrack(cnt)
                cnt[i] += 1

        return sum_
