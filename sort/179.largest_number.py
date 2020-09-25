"""
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:
Input: [10,2]
Output: "210"

Example 2:
Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
"""


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ""
            
        res = self.mergeSort(nums) 
        res = "".join(map(str, res))
        
        return res.lstrip("0") or "0"
        
    
    def mergeSort(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        
        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        
        return self.merge(left, right)
    
    
    def merge(self, l1: List[int], l2: List[int]) -> List[int]:
        res = [] 
        i = j = 0
        
        while i < len(l1) and j < len(l2):
            if str(l1[i]) + str(l2[j]) > str(l2[j]) + str(l1[i]):
                res.append(l1[i])
                i += 1
            else:
                res.append(l2[j])
                j += 1
                
        res += l1[i:] or l2[j:]
        
        return res
