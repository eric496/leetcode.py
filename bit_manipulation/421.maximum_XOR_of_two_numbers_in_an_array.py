"""
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.
Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.
Could you do this in O(n) runtime?

Example:
Input: [3, 10, 5, 25, 2, 8]
Output: 28
Explanation: The maximum result is 5 ^ 25 = 28.
"""


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = 0
        mask = 0 
        
        for i in range(31, -1, -1):
            mask |= 1 << i
            lookup = set()
            
            for num in nums:
                lookup.add(num & mask)
                
            want = res | (1 << i)
            
            for prefix in lookup:
                if want ^ prefix in lookup:
                    res = want
                    
        return res
