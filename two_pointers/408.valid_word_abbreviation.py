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
        i = j = 0
        m, n = len(word), len(abbr)

        while i < m and j < n:
            if abbr[j].isdigit():
                if int(abbr[j]) == 0:
                    return False
                
                val = 0
                while j < n and abbr[j].isdigit():
                    val = val * 10 + int(abbr[j])
                    j += 1
                
                i += val
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        
        return i == m and j == n
