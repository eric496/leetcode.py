"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.
A valid IP address consists of exactly four integers (each integer is between 0 and 255) separated by single points.

Example:
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s or len(s) > 12:
            return []

        res = []
        self.backtrack(s, 0, [], res)

        return res

    def backtrack(self, s: str, ix: int, cur: List[str], res: List[str]) -> None:

        if len(cur) == 4 and ix == len(s):
            res.append(".".join(cur))
            return

        for i in range(1, 4):
            if ix + i > len(s):
                break

            target = s[ix : ix + i]

            if len(target) > 1 and target.startswith("0") or int(target) > 255:
                continue

            cur.append(target)
            self.backtrack(s, ix + i, cur, res)
            cur.pop()
