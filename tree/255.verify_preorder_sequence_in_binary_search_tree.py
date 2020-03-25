"""
Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.
You may assume each number in the sequence is unique.
Consider the following binary search tree: 

     5
    / \
   2   6
  / \
 1   3

Example 1:
Input: [5,2,6,1,3]
Output: false

Example 2:
Input: [5,2,1,3,6]
Output: true

Follow up:
Could you do it using only constant space complexity?
"""


# Solution 1: O(n) TC and O(n) SC
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stk = []
        low = float('-inf')
        
        for p in preorder:
            if p < low:
                return False
            
            while stk and p > stk[-1]:
                low = stk.pop()
            
            stk.append(p)
        
        return True


# Follow up: O(n) TC and O(1) SC
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        low = float('-inf')
        i = 0
        
        for p in preorder:
            if p < low:
                return False
            
            while i>0 and p > preorder[i-1]:
                low = preorder[i-1]
                i -= 1
                
            preorder[i] = p
            i += 1
            
        return True
        