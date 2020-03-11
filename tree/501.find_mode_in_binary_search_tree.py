"""
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: O(n) space
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        freq = {}
        self.dfs(root, freq)
        res, max_freq = [], 0
        
        for k,v in freq.items():
            if v > max_freq:
                max_freq = v
                res = [k]
            elif v == max_freq:
                res.append(k)
                
        return res
        
        
    def dfs(self, node: TreeNode, freq: dict) -> None:
        if not node:
            return
        
        freq[node.val] = freq.get(node.val, 0) + 1
        self.dfs(node.left, freq)
        self.dfs(node.right, freq)


# Solution 2: O(1) space
class Solution:
    def __init__(self):
        self.prev = None
        self.cur_freq = 0
        self.max_freq = 0
        self.res = []
    
    
    def findMode(self, root: TreeNode) -> List[int]:
        self.dfs(root)
        
        return self.res
        

    # inorder traversal    
    def dfs(self, node: TreeNode) -> None:
        if not node:
            return
        
        self.dfs(node.left)
        
        if node.val != self.prev:
            self.cur_freq = 1
        else:
            self.cur_freq += 1
        
        if self.cur_freq == self.max_freq:
            self.res.append(node.val)
        elif self.cur_freq > self.max_freq:
            self.res = [node.val]
            self.max_freq = self.cur_freq
            
        self.prev = node.val
        
        self.dfs(node.right)
        