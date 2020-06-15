"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2

Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = {0: 1}
        presum = res = 0

        for num in nums:
            presum += num

            if presum - k in cnt:
                res += cnt[presum - k]

            cnt[presum] = cnt.get(presum, 0) + 1

        return res
