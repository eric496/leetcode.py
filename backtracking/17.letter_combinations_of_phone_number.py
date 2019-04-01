"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        d = {
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
        self.backtrack(digits, d, 0, "", res)
        
        return res
        
        
    def backtrack(self, digits: str, d: dict, dix: int, path: str, res: List[str]) -> None:
        if len(path) == len(digits):
            res.append(path)
            return
        else:
            for ch in d[digits[dix]]:
                cur_path = path
                path += ch
                self.backtrack(digits, d, dix+1, path, res)
                path = cur_path
