"""
You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'.
A string is said to be balanced if each of its characters appears n/4 times where n is the length of the string.
Return the minimum length of the substring that can be replaced with any other string of the same length to make the original string s balanced.
Return 0 if the string is already balanced.

Example 1:
Input: s = "QWER"
Output: 0
Explanation: s is already balanced.

Example 2:
Input: s = "QQWE"
Output: 1
Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.

Example 3:
Input: s = "QQQW"
Output: 2
Explanation: We can replace the first "QQ" to "ER". 

Example 4:
Input: s = "QQQQ"
Output: 3
Explanation: We can replace the last 3 'Q' to make s = "QWER".

Constraints:
1 <= s.length <= 10^5
s.length is a multiple of 4
s contains only 'Q', 'W', 'E' and 'R'.
"""


# Solution 1
class Solution:
    def balancedString(self, s: str) -> int:
        cnt = [0] * 26
        n = len(s)

        for c in s:
            cnt[ord(c) - ord("A")] += 1

        equal = n // 4

        for i in range(len(cnt)):
            cnt[i] = cnt[i] - equal if cnt[i] > equal else 0

        start = end = 0
        res = n

        while end < len(s):
            cnt[ord(s[end]) - ord("A")] -= 1

            while start < n and all(x <= 0 for x in cnt):
                res = min(res, end - start + 1)
                cnt[ord(s[start]) - ord("A")] += 1
                start += 1

            end += 1

        return res


# Solution 2
class Solution:
    def balancedString(self, s):
        cnt = {"Q": 0, "W": 0, "R": 0, "E": 0}

        for c in s:
            cnt[c] += 1

        res = n = len(s)
        start = 0

        for end, c in enumerate(s):
            cnt[c] -= 1

            while start < n and all(n // 4 >= cnt[c] for c in "QWER"):
                res = min(res, end - start + 1)
                cnt[s[start]] += 1
                start += 1

        return res
