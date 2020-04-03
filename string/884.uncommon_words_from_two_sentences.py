"""
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Return a list of all uncommon words. 
You may return the list in any order.

Example 1:
Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]

Example 2:
Input: A = "apple apple", B = "banana"
Output: ["banana"]
"""

# Solution 1: Hashmap
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        A, B = A.split(), B.split()
        cnt = {}
        res = []

        for a in A:
            cnt[a] = 0 if a in cnt else 1

        for b in B:
            cnt[b] = 0 if b in cnt else 1

        for c in cnt:
            if cnt[c]:
                res.append(c)

        return res


# Solution 2: Concatenate two sentences
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        C = A + " " + B
        C = C.split()
        cnt = {}
        res = []

        for c in C:
            cnt[c] = cnt.get(c, 0) + 1

        for word in cnt:
            if cnt[word] == 1:
                res.append(word)

        return res
