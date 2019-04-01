'''
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]

Follow up:
Could you optimize your algorithm to use only O(k) extra space?
'''

# Recursive
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]*(n+1) for n in range(rowIndex+1)]
        
        if rowIndex < 2:
            return res[-1]
        
        self.recurse(2, res)
        
        return res[-1]
        
    def recurse(self, rowIndex: int, res) -> None:
        if rowIndex >= len(res):
            return
        
        for i in range(1, len(res[rowIndex])-1):
            res[rowIndex][i] = res[rowIndex-1][i-1] + res[rowIndex-1][i]
            
        self.recurse(rowIndex+1, res)

# Iterative
class Solution:
    def getRow(self, rowIndex: int) -> list:
        row = [1]

        for _ in range(rowIndex):
            row = [x+y for x,y in zip([0]+row, row+[0])]
        
        return row