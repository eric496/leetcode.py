"""
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.
You may return the answer in any order.

Example 1:
Input: ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: ["cool","lock","cook"]
Output: ["c","o"]
 
Note:
1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
"""


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        min_freq = [float("inf")] * 26

        for word in A:
            freq = [0] * 26

            for ch in word:
                freq[ord(ch) - ord("a")] += 1

            for i, f in enumerate(freq):
                min_freq[i] = min(f, min_freq[i])

        res = []

        for i, freq in enumerate(min_freq):
            if freq:
                res += [chr(i + ord("a"))] * freq

        return res
