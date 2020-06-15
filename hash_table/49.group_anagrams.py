"""
Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
All inputs will be in lowercase.
The order of your output does not matter.
"""


# Solution 1: sort each string - O(nlogn) TC and O(n) TC
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            sort = "".join(sorted(s))

            if sort in d:
                d[sort].append(s)
            else:
                d[sort] = [s]

        return d.values()


# Solution 2: use direct address hashtable - O(n) TC where n is the number of characters from all strings
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            d = [0] * 26

            for c in s:
                d[ord(c) - ord("a")] += 1

            key = tuple(d)

            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]

        return res.values()
