"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.
"""


# Solution 1
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        aux = {0: 0}
        res = 0
        cnt = 0
        
        for i, n in enumerate(nums):
            cnt += 1 if n else -1
            
            if cnt in aux:
                res = max(res, i - aux[cnt] + 1)
            else:
                aux[cnt] = i + 1
                
        return res


# Solution 2: prefix sum
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {}
        presum = res = 0
        
        for i, n in enumerate(nums):
            presum += 1 if n else -1
            
            if presum == 0:
                res = i + 1
            elif presum in mp:
                res = max(res, i - mp[presum])
            else:
                mp[presum] = i
                
        return res
        