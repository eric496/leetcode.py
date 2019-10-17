"""
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:
Input: 12
Output: 21

Example 2:
Input: 21
Output: -1
"""

# Reference: 
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(map(int, str(n)))
        
        for i in range(len(s)-1, 0, -1):
            if s[i-1] < s[i]:
                right_min = float('inf')
                min_idx = None
                for j in range(i, len(s)):
                    if s[j] > s[i-1] and s[j] < right_min:
                        right_min = s[j]
                        min_idx = j
                s[i-1], s[min_idx] = s[min_idx], s[i-1]
                s[i:] = sorted(s[i:])
                break
                
        res = ''.join(str(ch) for ch in s)
        
        return int(res) if int(res) != n and int(res) < 2**31 else -1
