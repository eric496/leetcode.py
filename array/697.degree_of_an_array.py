'''
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6

Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
'''

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        res = {}

        for ix, n in enumerate(nums):
            if res.get(n):
                res[n][0] += 1
                res[n][2] = ix - res[n][1] + 1
            else:
                res[n] = [1, ix, 1]

        max_cnt, length = [], 0

        for val in res.values():
            if not max_cnt:
                max_cnt.append(val)
            elif val[0] > max_cnt[0][0]:
                max_cnt.clear()
                max_cnt.append(val)
            elif val[0] == max_cnt[0][0]:
                max_cnt.append(val)

        return sorted(max_cnt, key=lambda x: x[-1])[0][-1]

