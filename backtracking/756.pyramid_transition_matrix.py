"""
We are stacking blocks to form a pyramid. Each block has a color which is a one letter string.
We are allowed to place any color block C on top of two adjacent blocks of colors A and B, if and only if ABC is an allowed triple.
We start with a bottom row of bottom, represented as a single string. We also start with a list of allowed triples allowed. Each allowed triple is represented as a string of length 3.
Return true if we can build the pyramid all the way to the top, otherwise false.

Example 1:
Input: bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"]
Output: true
Explanation:
We can stack the pyramid like this:
    A
   / \
  G   E
 / \ / \
B   C   D
We are allowed to place G on top of B and C because BCG is an allowed triple.  Similarly, we can place E on top of C and D, then A on top of G and E.

Example 2:
Input: bottom = "AABA", allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
Output: false
Explanation:
We can't stack the pyramid to the top.
Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.

Note:
bottom will be a string with length in range [2, 8].
allowed will have length in range [0, 200].
Letters in all strings will be chosen from the set {'A', 'B', 'C', 'D', 'E', 'F', 'G'}.
"""


from collections import defaultdict


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        mp = defaultdict(set)
        
        for a in allowed:
            mp[a[:2]].add(a[-1])
            
        return self.dfs(bottom, mp)
        
    def dfs(self, bottom: str, mp: dict) -> bool:
        if len(bottom) == 1:
            return True
        
        for i in range(len(bottom) - 1):
            if bottom[i:i+2] not in mp:
                return False
        
        res = []
        self.backtrack(bottom, 0, [], res, mp)
        
        for s in res:
            if self.dfs(s, mp):
                return True
            
        return False
    
    def backtrack(self, bottom: str, i: int, cur: List[str], res: List[str], mp: dict) -> None:
        if i == len(bottom) - 1:
            res.append("".join(cur))
            return 
        
        for c in mp[bottom[i: i+2]]:
            cur.append(c)
            self.backtrack(bottom, i + 1, cur, res, mp)
            cur.pop()
            