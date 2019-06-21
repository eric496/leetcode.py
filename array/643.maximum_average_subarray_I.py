"""
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
 
Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
"""

"""
Thought process:
    Use a sliding window, at each iteration, remove the first element in the window and add one more to the end.
    Update global maximum at each iteration.
"""


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_ = cur = sum(nums[:k])
        
        for i in range(1, len(nums)-k+1):
            cur -= nums[i-1]
            cur += nums[i+k-1]
            max_ = max(max_, cur)
            
        return max_ / k
