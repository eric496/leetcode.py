"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
Note: The algorithm should run in linear time and in O(1) space.

Example 1:
Input: [3,2,3]
Output: [3]

Example 2:
Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        me1 = me2 = None
        cnt1 = cnt2 = 0
        
        for num in nums:
            if num == me1:
                cnt1 += 1
            elif num == me2:
                cnt2 += 1
            elif cnt1 == 0:
                me1 = num
                cnt1 = 1
            elif cnt2 == 0:
                me2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        return [me for me in (me1, me2) if nums.count(me) > len(nums)//3]
