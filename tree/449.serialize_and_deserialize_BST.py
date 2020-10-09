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

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        self.sdfs(root, res)
        
        return "".join(res)
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        q = deque([x for x in data.split("#")])
        
        return self.ddfs(q, float("-inf"), float("inf"))
    
    
    def sdfs(self, root: TreeNode, res: List[str]) -> None:
        if root:
            res.append(str(root.val))
            res.append("#")
            self.sdfs(root.left, res)
            self.sdfs(root.right, res)
        else:
            res.append("X")
            res.append("#")
            
    
    def ddfs(self, q: deque, lo: int, hi: int) -> TreeNode:
        if not q:
            return None
        
        val = q.popleft()
        
        if val == "X":
            return None
        elif lo <= int(val) <= hi:
            root = TreeNode(int(val))
            root.left = self.ddfs(q, lo, int(val))
            root.right = self.ddfs(q, int(val), hi)
            
            return root   
