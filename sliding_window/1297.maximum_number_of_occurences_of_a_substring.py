"""
Given a string s, return the maximum number of ocurrences of any substring under the following rules:
The number of unique characters in the substring must be less than or equal to maxLetters.
The substring size must be between minSize and maxSize inclusive.

Example 1:
Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
Output: 2
Explanation: Substring "aab" has 2 ocurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).

Example 2:
Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
Output: 2
Explanation: Substring "aaa" occur 2 times in the string. It can overlap.

Example 3:
Input: s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
Output: 3

Example 4:
Input: s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
Output: 0

Constraints:
1 <= s.length <= 10^5
1 <= maxLetters <= 26
1 <= minSize <= maxSize <= min(26, s.length)
s only contains lowercase English letters.
"""


# Solution 1: brute force
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        cnt = {}
        
        for i in range(len(s) - minSize + 1):
            target = s[i:i+minSize]
            
            if target in cnt:
                cnt[target] += 1
            elif self.unique_count(target) <= maxLetters:
                cnt[target] = 1
                
        return max(cnt.values()) if cnt else 0
        
        
    def unique_count(self, s: str) -> int:
        cnt = [0] * 26
        
        for c in s:
            cnt[ord(c) - ord("a")] += 1
            
        return sum(1 for n in cnt if n)


# Solution 2: sliding window
