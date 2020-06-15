"""
You have k lists of sorted integers in ascending order. Find the smallest range that includes at least one number from each of the k lists.
We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

Example 1:
Input: [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].

Note:
The given list may contain duplicates, so ascending order means >= here.
1 <= k <= 3500
-105 <= value of elements <= 105.
"""


import heapq


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(pq)
        res = [-1e5, 1e5]
        right = max(row[0] for row in nums)

        while pq:
            left, r, c = heapq.heappop(pq)

            if right - left < res[1] - res[0]:
                res = [left, right]

            if c + 1 == len(nums[r]):
                return res

            right = max(right, nums[r][c + 1])
            heapq.heappush(pq, (nums[r][c + 1], r, c + 1))

        return res
