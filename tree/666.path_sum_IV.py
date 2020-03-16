"""
If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.
For each integer in this list:
The hundreds digit represents the depth D of this node, 1 <= D <= 4.
The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The position is the same as that in a full binary tree.
The units digit represents the value V of this node, 0 <= V <= 9.
Given a list of ascending three-digits integers representing a binary tree with the depth smaller than 5, you need to return the sum of all paths from the root towards the leaves.

Example 1:
Input: [113, 215, 221]
Output: 12
Explanation: 
The tree that the list represents is:
    3
   / \
  5   1
The path sum is (3 + 5) + (3 + 1) = 12.

Example 2:
Input: [113, 221]
Output: 4
Explanation: 
The tree that the list represents is: 
    3
     \
      1
The path sum is (3 + 1) = 4.
"""


class Solution:
    def pathSum(self, nums: List[int]) -> int:
        lookup = {n//10: n%10 for n in nums}
        res = [0]
        self.dfs(nums[0]//10, 0, lookup, res)
        
        return res[0]
        
        
    def dfs(self, val: int, presum: int, lookup: dict, res: List[int]) -> None:
        depth, pos = divmod(val, 10)
        cur = presum + lookup[val]
        left = (depth+1) * 10 + (2*pos-1)
        right = (depth+1) * 10 + 2*pos
        
        if left not in lookup and right not in lookup:
            res[0] += cur
            return
            
        if left in lookup:
            self.dfs(left, cur, lookup, res)
            
        if right in lookup:
            self.dfs(right, cur, lookup, res)
