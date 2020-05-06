"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""


# Solution 1: O(n) time and O(n) space by using a map
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = {}
        half_size = len(nums) // 2
        
        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1
            
            # Early stopping
            if cnt[num] > half_size:
                return num


# Solution 2: Boyer-Moore majority vote algorithm - O(n) TC and O(1) SC
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = nums[0]
        cnt = 0
        
        for num in nums:
            if num == major:
                cnt += 1
            else:
                cnt -= 1
                
                if cnt == 0:
                    major = num
                    cnt = 1
                    
        return major


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        cnt = 1 
        
        for i in range(1, len(nums)):
            if cnt == 0:
                majority = nums[i]
                cnt = 1
            elif nums[i] == majority:
                cnt += 1
            elif nums[i] != majority:
                cnt -= 1
        
        return majority


# Solution 3: sort - O(nlogn) TC and O(n) SC
class Solution:
    def majorityElement(self, nums: list) -> int:
        return sorted(nums)[len(nums) // 2]
