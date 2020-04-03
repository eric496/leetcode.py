"""
Given a string S, return the number of substrings of length K with no repeated characters.

Example 1:
Input: S = "havefunonleetcode", K = 5
Output: 6
Explanation: 
There are 6 substrings they are : 'havef','avefu','vefun','efuno','etcod','tcode'.

Example 2:
Input: S = "home", K = 5
Output: 0
Explanation: 
Notice K can be larger than the length of S. In this case is not possible to find any substring.

Note:
1 <= S.length <= 10^4
All characters of S are lowercase English letters.
1 <= K <= 10^4
"""


class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        if K >= len(S):
            return 0

        cnt, res = {}, 0

        for ch in S[:K]:
            cnt[ch] = cnt.get(ch, 0) + 1

        if len(cnt) == K:
            res += 1

        for i in range(K, len(S)):
            pre, cur = S[i - K], S[i]

            if cnt[pre] == 1:
                del cnt[pre]
            else:
                cnt[pre] -= 1

            cnt[cur] = cnt.get(cur, 0) + 1

            if len(cnt) == K:
                res += 1

        return res
