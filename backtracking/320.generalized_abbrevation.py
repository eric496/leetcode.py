"""
Write a function to generate the generalized abbreviations of a word. 
Note: The order of the output does not matter.

Example:
Input: "word"
Output:
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
"""


class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []
        self.backtrack(word, [], 0, 0, res)
        
        return res
        
    def backtrack(self, word: str, cur: List[str], pos: int, cnt: int, res: List[str]) -> None:
        if pos == len(word):
            if cnt:
                cur.append(str(cnt))
                
            res.append("".join(cur))
            
            return 
        
        self.backtrack(word, cur, pos + 1, cnt + 1, res)
        
        cur.pop()
        
        if cnt:
            cur.append(str(cnt))
        
        self.backtrack(word, cur + [word[pos]], pos + 1, 0, res)
