'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''

# O(n) time using map
class Solution:
    def singleNumber(self, nums: list) -> int:
        count = {}
        
        for n in nums:
            if n in count:
                count[n] -= 1
            else:
                count[n] = 1
        
        for k,v in count.items():
            if v == 1:
                return k
        return 0

# Bit operation
class Solution:
    def singleNumber(self, nums: list) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res

# One-liner solution
class Solution:
    def singleNumber(self, nums: list) -> int:
        return sum(set(nums))*2 - sum(nums)
