"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.
You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""

# Solution 1: Sorting - O(nlgn) TC, O(n) SC
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sort = sorted(nums)
        start, end = 0, len(nums) - 1

        while start < len(nums) and nums[start] == sort[start]:
            start += 1

        while end > start and nums[end] == sort[end]:
            end -= 1

        return end - start + 1


# Solution 2: O(n) TC, O(1) SC
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        length, start, end, max_so_far, min_so_far = len(nums), 0, 0, nums[0], nums[-1]

        for i, n in enumerate(nums[1:], 1):
            max_so_far = max(max_so_far, n)
            min_so_far = min(min_so_far, nums[length - 1 - i])
            if max_so_far > n:
                end = i
            if min_so_far < nums[length - 1 - i]:
                start = len(nums) - 1 - i

        return end - start + 1 if end else 0
