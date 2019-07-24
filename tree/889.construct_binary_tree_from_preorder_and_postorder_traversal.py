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
