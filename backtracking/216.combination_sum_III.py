"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:
All numbers will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.backtrack(k, n, 1, [], res)
        
        return res
    
        
    def backtrack(self, k: int, n: int, start: int, cur: List[int], res: List[List[int]]) -> None:
        if len(cur) > k:
            return 
        
        if len(cur) == k and n == 0:
            res.append(list(cur))
            return
        
        for i in range(start, 10):
            if n - i >= 0:
                cur.append(i)
                self.backtrack(k, n-i, i+1, cur, res)
                cur.pop()
            