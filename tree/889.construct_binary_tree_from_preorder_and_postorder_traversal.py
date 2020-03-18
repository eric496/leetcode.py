"""
Return any binary tree that matches the given preorder and postorder traversals.
Values in the traversals pre and post are distinct positive integers.

Example 1:
Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]

Note:
1 <= pre.length == post.length <= 30
pre[] and post[] are both permutations of 1, 2, ..., pre.length.
It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: recursive
class Solution:
    def __init__(self):
        self.pre_idx = 0
        self.pos_idx = 0
        
        
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        root = TreeNode(pre[self.pre_idx])
        self.pre_idx += 1
        
        if root.val != post[self.pos_idx]:
            root.left = self.constructFromPrePost(pre, post)
            
        if root.val != post[self.pos_idx]:
            root.right = self.constructFromPrePost(pre, post)
            
        self.pos_idx += 1    
        
        return root


# Solution 1: another recursive
class Solution:      
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        lookup = {v: i for i,v in enumerate(post)}
        
        return self.dfs(pre, 0, len(pre)-1, post, 0, len(post)-1, lookup)
        
        
    def dfs(self, pre: List[int], pre_start: int, pre_end: int, post: List[int], post_start: int, post_end: int, lookup: dict) -> TreeNode:
        if pre_start > pre_end or post_start > post_end:
            return None
        
        root = TreeNode(pre[pre_start])
        
        if pre_start < pre_end:
            diff = lookup[pre[pre_start+1]] - post_start
            root.left = self.dfs(pre, pre_start+1, pre_start+1+diff, post, post_start, post_start+diff, lookup)
            root.right = self.dfs(pre, pre_start+1+diff+1, pre_end, post, post_start+diff+1, post_end-1, lookup)
            
        return root


# Solution 2: iterative
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        stk = [TreeNode(pre[0])]
        i = 0
        
        for val in pre[1:]:
            node = TreeNode(val)
            
            while stk[-1].val == post[i]:
                stk.pop()
                i += 1
            
            if not stk[-1].left:
                stk[-1].left = node
            else:
                stk[-1].right = node
            
            stk.append(node)
            
        return stk[0]
