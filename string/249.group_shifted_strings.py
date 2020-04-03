"""
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:
"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:
Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
"""


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        pattern = {}

        for s in strings:
            key = []

            for i in range(1, len(s)):
                offset = ord(s[i]) - ord(s[i - 1])

                if offset < 0:
                    key.append(offset + 26)
                else:
                    key.append(offset)

            key = "-".join(map(str, key))
            pattern[key] = pattern.get(key, []) + [s]

        return list(pattern.values())
