"""
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]

Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:
S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
"""


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S:
            return []
        
        last = {c: i for i, c in enumerate(S)}
        left = right = 0
        res = []
        
        for i, c in enumerate(S):
            right = max(right, last[c])
            
            if right == i:
                res.append(right - left + 1)
                left = right + 1
        
        return res
