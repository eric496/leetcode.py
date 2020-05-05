"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.
"""

# Solution 1 - O(n) TC and O(n) SC
class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = [0] * len(s)
        seen = {}
        
        for i, c in enumerate(s):
            cnt[seen.get(c, i)] += 1
            
            if c not in seen:
                seen[c] = i
                
        for i, n in enumerate(cnt):
            if n == 1:
                return i
        
        return -1


# Solution 2 - O(n) TC and O(1) SC
class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - ord("a")] += 1

        for i, c in enumerate(s):
            if cnt[ord(c) - ord("a")] == 1:
                return i

        return -1
