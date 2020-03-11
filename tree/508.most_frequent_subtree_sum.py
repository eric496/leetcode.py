"""
Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:
  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.

Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.

Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        subsum = {}
        self.dfs(root, subsum)
        max_freq = max(subsum.values())
        
        return [k for k,v in subsum.items() if v==max_freq]
        
        
    def dfs(self, node: TreeNode, subsum: dict) -> int:
        if not node:
            return 0
        
        left = self.dfs(node.left, subsum)
        right = self.dfs(node.right, subsum)
        sub = node.val + left + right
        subsum[sub] = subsum.get(sub, 0) + 1
        
        return sub
        