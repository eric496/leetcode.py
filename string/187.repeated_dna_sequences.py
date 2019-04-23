"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC", "CCCCCAAAAA"]
"""

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = {}
        
        for i in range(len(s)-9):
            if s[i:i+10] in d:
                d[s[i:i+10]] += 1
            else:
                d[s[i:i+10]] = 1
        
        res = []
        
        for k, v in d.items():
            if v > 1:
                res.append(k)
                
        return res

# More concise: one pass
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = {}
        res = []
        
        for i in range(len(s)-9):
            if s[i:i+10] in d:
                if d[s[i:i+10]] == 1:
                    res.append(s[i:i+10])
                d[s[i:i+10]] += 1                    
            else:
                d[s[i:i+10]] = 1
         
        return res
    