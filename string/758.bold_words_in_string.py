"""
Given a set of keywords words and a string S, make all appearances of all keywords in S bold. Any letters between <b> and </b> tags become bold.
The returned string should use the least number of tags possible, and of course the tags should form a valid combination.
For example, given that words = ["ab", "bc"] and S = "aabcd", we should return "a<b>abc</b>d". Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.

Note:
words has length in range [0, 50].
words[i] has length in range [1, 10].
S has length in range [0, 500].
All characters in words[i] and S are lowercase letters.
"""


class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        bold = [False] * (len(S) + 1)

        for word in words:
            start = S.find(word)

            while start != -1:
                bold[start : start + len(word)] = [True] * len(word)
                start = S.find(word, start + 1)

        res = ["<b>"] if bold[0] else []

        for i in range(len(bold) - 1):
            res.append(S[i])

            if not bold[i] and bold[i + 1]:
                res.append("<b>")
            elif bold[i] and not bold[i + 1]:
                res.append("</b>")

        return "".join(res)
