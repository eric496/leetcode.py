"""
Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.

Note:
The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
"""


# Remainder theorem: (a + n*x) % x == a % x
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        ix, cumsum = {0: -1}, 0

        for i, num in enumerate(nums):
            cumsum += num

            if k:
                cumsum %= k

            prev = ix.get(cumsum)

            if prev is not None:
                if i - prev > 1:
                    return True
            else:
                ix[cumsum] = i

        return False
