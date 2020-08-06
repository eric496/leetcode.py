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
        cnt = {}

        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1

        res = []

        for k, v in cnt.items():
            if v > 1:
                res.append(k)

        return res


# O(n) TC and O(1) SC
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        
        for num in nums:
            if nums[abs(num)-1] < 0:
                res.append(abs(num))
            else:
                nums[abs(num)-1] *= -1
                
        return res
