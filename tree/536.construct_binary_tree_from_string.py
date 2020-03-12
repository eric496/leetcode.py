"""
You need to construct a binary tree from a string consisting of parenthesis and integers.
The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.
You always start to construct the left child node of the parent first if it exists.

Example:
Input: "4(2(3)(1))(6(5))"
Output: return the tree root node representing the following tree:
       4
     /   \
    2     6
   / \   / 
  3   1 5   

Note:
There will only be '(', ')', '-' and '0' ~ '9' in the input string.
An empty tree is represented by "" instead of "()".
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def str2tree(self, s: str) -> TreeNode:
        stk = []
        start = walker = 0
        
        while walker < len(s):
            if s[walker].isdigit() or s[walker] == '-':
                while walker+1 < len(s) and s[walker+1].isdigit():
                    walker += 1
                
                node = TreeNode(int(s[start:walker+1]))
                
                if stk:
                    if stk[-1].left:
                        stk[-1].right = node
                    else:
                        stk[-1].left = node
                        
                stk.append(node)
            elif s[walker] == ')':
                stk.pop()
                                
            walker += 1
            start = walker
                    
        return stk[-1] if stk else None
