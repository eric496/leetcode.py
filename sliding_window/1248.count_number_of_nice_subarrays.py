"""
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
Return the number of nice sub-arrays.

Example 1:
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.

Example 3:
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16

Constraints:
1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
"""


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = right = 0
        n = len(nums)
        odd = 0
        res = 0
        
        while right < n:
            odd += 1 if nums[right]&1 else 0
            
            while left < right and odd > k:
                if nums[left] & 1:
                    odd -= 1
                    
                left += 1
                
            if odd == k:
                res += 1
                i = left
                
                while i < right and nums[i]&1 == 0:
                    res += 1
                    i += 1
                    
            right += 1
            
        return res
        