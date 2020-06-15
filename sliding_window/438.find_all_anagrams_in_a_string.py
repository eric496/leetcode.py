"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

Example 1:
Input:
s: "cbaebabacd" p: "abc"
Output:
[0, 6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input:
s: "abab" p: "ab"
Output:
[0, 1, 2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""


# Sliding window: O(n) TC, O(1) SC
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or len(s) < len(p):
            return []

        cnt = [0] * 26

        for c in p:
            cnt[ord(c) - ord("a")] += 1

        start = end = 0
        need = len(p)
        res = []

        while end < len(s):
            if cnt[ord(s[end]) - ord("a")] >= 1:
                need -= 1

            cnt[ord(s[end]) - ord("a")] -= 1

            if need == 0:
                res.append(start)

            if end - start + 1 == len(p):
                if cnt[ord(s[start]) - ord("a")] >= 0:
                    need += 1

                cnt[ord(s[start]) - ord("a")] += 1
                start += 1

            end += 1

        return res
