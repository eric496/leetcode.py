"""
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

Example:
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s: 
            return []
        
        res = []
        self.backtrack(s, 0, [], res)
        
        return res
        
        
    def backtrack(self, s: str, start: int, cur_res: List[str], res: List[List[int]]) -> None:
        if len(cur_res) > 0 and start == len(s):
            res.append(list(cur_res))
        
        for i in range(start, len(s)):
            if self.is_palindrome(s[start:i+1]):
                if i == start:
                    cur_res.append(s[i])
                else:
                    cur_res.append(s[start:i+1])
                
                self.backtrack(s, i+1, cur_res, res)
                cur_res.pop()
    
    
    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]
        