"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""


# Solution 1: DFS
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        mp = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }
        
        res = []
        self.dfs(digits, 0, "", mp, res)
        
        return res
        
    def dfs(self, digits: str, i: int, cur: str, mp: dict, res: List[str]) -> None:
        if i == len(digits):
            res.append(cur)
            return 
            
        for c in mp[int(digits[i])]:
            self.dfs(digits, i + 1, cur + c, mp, res)
            

# Solution 2: backtrack
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mp = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        self.backtrack(digits, 0, "", mp, res)

        return res

    def backtrack(
        self, digits: str, i: int, path: str, mp: dict, res: List[str]
    ) -> None:
        if len(path) == len(digits):
            res.append(path)
            return
        
        for c in mp[digits[i]]:
            path += c
            self.backtrack(digits, i + 1, path, mp, res)
            path = path[:-1]
