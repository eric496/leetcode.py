"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.
The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque

class Codec:

    def serialize(self, root):
        res = []
        self.serialize_dfs(root, res)
        return ''.join(res)
        

    def deserialize(self, data):
        q = deque([x for x in data.split('#') if x])
        return self.deserialize_dfs(q, float('-inf'), float('inf'))
        
        
    def serialize_dfs(self, root, res):
        if root:
            res.append(str(root.val) + '#')
            self.serialize_dfs(root.left, res)
            self.serialize_dfs(root.right, res)
            
            
    def deserialize_dfs(self, q, low, high):
        if q and low <= int(q[0]) <= high:
            val = int(q.popleft())
            root = TreeNode(val)
            root.left = self.deserialize_dfs(q, low, val)
            root.right = self.deserialize_dfs(q, val, high)
            return root
