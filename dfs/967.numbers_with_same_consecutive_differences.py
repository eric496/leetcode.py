"""
Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.
Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.
You may return the answer in any order.

Example 1:
Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.

Example 2:
Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

Note:
1 <= N <= 9
0 <= K <= 9
"""


class Solution:
    
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1:
            return list(range(10))
        
        res = []
        
        for num in range(1, 10):
            self.dfs(N - 1, num, K, res)
            
        return res
    

    def dfs(self, N: int, num: int, K: int, res: List[int]) -> None:
        if N == 0:
            res.append(num)
            return
        
        if num % 10 + K < 10:
            self.dfs(N - 1, num*10 + num%10 + K, K, res)
            
        if K > 0 and num%10 - K >= 0:
            self.dfs(N - 1, num*10 + num%10 - K, K, res)
