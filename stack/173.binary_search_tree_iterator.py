"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
Calling next() will return the next smallest number in the BST.

Example:
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false

Note:
next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.
"""

"""
Thought process:
    1. Push all left nodes to a stack.
    2. When next() is called, pop the top element and push its right child in the same manner as step 1.
    3. When hasNext() is called, check if the stack is empty.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stk = []
        self.push(root)

        
    def next(self) -> int:
        node = self.stk.pop()
        self.push(node.right)
        return node.val

        
    def hasNext(self) -> bool:
        return True if self.stk else False
            
    
    def push(self, node: TreeNode) -> None:
        while node:
            self.stk.append(node)
            node = node.left
