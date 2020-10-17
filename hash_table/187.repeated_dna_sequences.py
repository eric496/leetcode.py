"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC", "CCCCCAAAAA"]
"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 11:
            return []

        cnt = {}
        n = len(s)

        for i in range(n - 9):
            seq = s[i:i+10]
            cnt[seq] = cnt.get(seq, 0) + 1

        res = []

        for k, v in cnt.items():
            if v > 1:
                res.append(k)

        return res


# More concise: one pass
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 11:
            return []
        
        cnt = {}
        res = []
        n = len(s)
        
        for i in range(n-9):
            seq = s[i:i+10]
            
            if seq in cnt:
                if cnt[seq] == 1:
                    res.append(seq)
                    
            cnt[seq] = cnt.get(seq, 0) + 1
        
        return res


# Bit manipulation
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 11:
            return []
        
        words = set()
        seen = set()
        res = []
        n = len(s)
        mp = [0] * 26
        mp[ord("A")-ord("A")] = 0 #00
        mp[ord("C")-ord("A")] = 1 #01
        mp[ord("G")-ord("A")] = 2 #10
        mp[ord("T")-ord("A")] = 3 #11
        
        for i in range(n-9):
            seq = 0
            
            for j in range(i, i+10):
                seq <<= 2
                seq |= mp[ord(s[j])-ord("A")] 
                
            if seq in words:
                if seq not in seen:
                    res.append(s[i:i+10])
                    seen.add(seq)
            else:
                words.add(seq)
                
        return res
        