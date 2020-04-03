"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.

Example 2:
Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
"""


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        res = []
        start = i = 0

        while i < len(nums) - 1:
            if nums[i] + 1 != nums[i + 1]:
                self.sum_range(start, i, nums, res)
                start = i + 1

            i = i + 1

        self.sum_range(start, i, nums, res)

        return res

    def sum_range(self, start: int, end: int, nums: List[int], res: List[str]) -> None:
        if start == end:
            res.append(str(nums[end]))
        else:
            res.append(str(nums[start]) + "->" + str(nums[end]))
