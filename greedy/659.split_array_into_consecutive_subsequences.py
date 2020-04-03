"""
Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.

Example 1:
Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5

Example 2:
Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5

Example 3:
Input: [1,2,3,4,4,5]
Output: False

Constraints:
1 <= nums.length <= 10000
"""


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        cnt, end = {}, {}

        for n in nums:
            cnt[n] = cnt.get(n, 0) + 1

        for n in nums:
            if not cnt.get(n):
                continue

            cnt[n] -= 1

            if end.get(n - 1):
                end[n - 1] -= 1
                end[n] = end.get(n, 0) + 1
            elif cnt.get(n + 1) and cnt.get(n + 2):
                cnt[n + 1] -= 1
                cnt[n + 2] -= 1
                end[n + 2] = end.get(n + 2, 0) + 1
            else:
                return False

        return True
