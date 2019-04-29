"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""

# O(n) TC and SC
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        cnt, res = {}, []
        
        for n in nums:
            cnt[n] = cnt.get(n, 0) + 1
        
        for k, v in cnt.items():
            if v > 1:
                res.append(k)
                
        return res

# O(n) TC and O(1) SC
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] > 0:
                nums[abs(nums[i])-1] *= -1
            else:
                res.append(abs(nums[i]))
        
        return res
        