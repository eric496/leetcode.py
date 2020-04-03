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
        if not nums:
            return []

        cnt1 = cnt2 = 0
        can1 = can2 = None

        for n in nums:
            if n == can1:
                cnt1 += 1
            elif n == can2:
                cnt2 += 1
            elif cnt1 == 0:
                cnt1, can1 = 1, n
            elif cnt2 == 0:
                cnt2, can2 = 1, n
            else:
                cnt1, cnt2 = cnt1 - 1, cnt2 - 1

        freq1, freq2 = nums.count(can1), nums.count(can2)

        if freq1 > len(nums) / 3 and freq2 > len(nums) / 3:
            return [can1, can2]
        elif freq1 > len(nums) / 3:
            return [can1]
        elif freq2 > len(nums) / 3:
            return [can2]
        else:
            return []
