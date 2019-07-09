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


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        cnt = {}
        self.dfs(root, cnt)
        max_cnt = max(cnt.values())
        
        return [sub for sub in cnt if cnt[sub] == max_cnt]
    
        
    def dfs(self, node: TreeNode, cnt: dict) -> int:
        if not node:
            return 0
        
        sub_sum = node.val + self.dfs(node.left, cnt) + self.dfs(node.right, cnt)
        cnt[sub_sum] = cnt.get(sub_sum, 0) + 1
        
        return sub_sum
        