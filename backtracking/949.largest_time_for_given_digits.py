"""
Given an array of 4 digits, return the largest 24 hour time that can be made.
The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.
Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

Example 1:
Input: [1,2,3,4]
Output: "23:41"

Example 2:
Input: [5,5,5,5]
Output: ""

Note:
A.length == 4
0 <= A[i] <= 9
"""


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        perm = []
        A.sort()
        self.backtrack(A, [], [0] * len(A), perm)
        candidates = []

        for p in perm:
            hour = p[0] * 10 + p[1]
            minute = p[2] * 10 + p[3]
            if 0 <= hour < 24 and 0 <= minute < 60:
                candidates.append(p)

        if not candidates:
            return ""

        candidates.sort()
        max_time = candidates[-1]
        max_time.insert(2, ":")

        return "".join(str(ch) for ch in max_time)


    def backtrack(
        self,
        A: List[int],
        cur_perm: List[int],
        visited: List[bool],
        perm: List[List[int]],
    ) -> None:
        if len(cur_perm) == len(A):
            perm.append(cur_perm[:])
        else:
            for ix, n in enumerate(A):
                if visited[ix]:
                    continue
                    
                if ix > 0 and n == A[ix - 1] and not visited[ix - 1]:
                    continue

                visited[ix] = 1
                cur_perm.append(n)
                self.backtrack(A, cur_perm, visited, perm)
                visited[ix] = 0
                cur_perm.pop()
