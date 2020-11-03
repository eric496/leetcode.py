"""
Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.
Return the power of the string.

Example 1:
Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.

Example 2:
Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

Example 3:
Input: s = "triplepillooooow"
Output: 5

Example 4:
Input: s = "hooraaaaaaaaaaay"
Output: 11

Example 5:
Input: s = "tourist"
Output: 1

Constraints:
1 <= s.length <= 500
s contains only lowercase English letters.
"""


# Solution 1: two pointers
class Solution:
    def maxPower(self, s: str) -> int:
        res = 0
        left = right = 0
        n = len(s)
        
        while right < n:
            while right < n and s[right] == s[left]:
                right += 1
                
            res = max(res, right - left)
            left = right
            
        return res


# Solution 2
class Solution:
    def maxPower(self, s: str) -> int:
        res = cnt = 1

        for i in range(1, len(s)):
            cnt = cnt + 1 if s[i] == s[i - 1] else 1
            res = max(res, cnt)

        return res
