"""
Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.
A string such as "word" contains only the following valid abbreviations:
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".

Note:
Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

Example 1:
Given s = "internationalization", abbr = "i12iz4n":
Return true.
Example 2:
Given s = "apple", abbr = "a2e":
Return false.
"""

"""
Thought process:
    Two pointers
"""


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = n = 0

        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                n = n * 10 + int(abbr[j])
                # Handle cases like "01"
                if n == 0:
                    return False
                j += 1
            else:
                i += n
                if i >= len(word) or word[i] != abbr[j]:
                    return False
                n = 0
                i += 1
                j += 1

        i += n

        return i == len(word) and j == len(abbr)
