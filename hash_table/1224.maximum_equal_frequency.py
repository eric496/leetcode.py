"""
Given an array nums of positive integers, return the longest possible length of an array prefix of nums, such that it is possible to remove exactly one element from this prefix so that every number that has appeared in it will have the same number of occurrences.
If after removing one element there are no remaining elements, it's still considered that every appeared number has the same number of ocurrences (0).

Example 1:
Input: nums = [2,2,1,1,5,3,3,5]
Output: 7
Explanation: For the subarray [2,2,1,1,5,3,3] of length 7, if we remove nums[4]=5, we will get [2,2,1,1,3,3], so that each number will appear exactly twice.

Example 2:
Input: nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
Output: 13

Example 3:
Input: nums = [1,1,1,2,2,2]
Output: 5

Example 4:
Input: nums = [10,2,8,9,3,8,1,5,2,3,7,6]
Output: 8

Constraints:
2 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
"""


from collections import defaultdict


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        num_cnt = defaultdict(int)
        freq_cnt = defaultdict(int)
        res = max_freq = 0
        
        for i, n in enumerate(nums):
            freq_cnt[num_cnt[n]] -= 1
            num_cnt[n] += 1
            freq_cnt[num_cnt[n]] += 1
            max_freq = max(max_freq, num_cnt[n])
            
            if max_freq == 1 or max_freq * freq_cnt[max_freq] == i or (max_freq - 1) * freq_cnt[max_freq - 1] + max_freq == i + 1:
                res = i + 1
                
        return res
        