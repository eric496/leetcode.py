"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.

Note:
The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur = max_ = 0

        for n in nums:
            if n:
                cur += 1
            else:
                max_ = max(max_, cur)
                cur = 0

        # Need to compare cur and max_ in case the last element of nums is 1
        return max_ if max_ > cur else cur
