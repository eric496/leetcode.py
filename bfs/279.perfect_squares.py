"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

# DP: TLE
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [float("inf")] * n

        for i in range(1, n + 1):
            min_, j = float("inf"), 1
            while j * j <= i:
                min_ = min(min_, dp[i - j * j] + 1)
                j += 1
            dp[i] = min_

        return dp[n]


# BFS
class Solution:
    def numSquares(self, n: int) -> int:
        q1, q2 = [0], []
        level = 0
        visited = [False] * (n + 1)

        while 1:
            level += 1
            for val in q1:
                i = 0
                while 1:
                    i += 1
                    total = val + i ** 2
                    if total == n:
                        return level
                    if total > n:
                        break
                    if visited[total]:
                        continue
                    q2.append(total)
                    visited[total] = True
            q1 = q2
            q2 = []

        return 0
