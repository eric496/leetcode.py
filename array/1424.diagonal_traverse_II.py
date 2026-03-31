"""
Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

Example 1:
Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]

Example 2:
Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]

Constraints:
    1 <= nums.length <= 105
    1 <= nums[i].length <= 105
    1 <= sum(nums[i].length) <= 105
    1 <= nums[i][j] <= 105
"""


# Solution 1 - sorting
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        tuples = []

        for r in range(len(nums)):
            for c in range(len(nums[r])):
                tuples.append((r+c, c, nums[r][c]))

        tuples.sort()

        return [v for _, _, v in tuples]
    
    
# Solution 2 - heap
import heapq


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        heap = []

        for r in range(len(nums)):
            for c in range(len(nums[r])):
                heapq.heappush(heap, (r+c, c, nums[r][c]))

        res = []

        while heap:
            res.append(heapq.heappop(heap)[2])

        return res


# Solution 3 - best performance
from collections import defaultdict


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        groups = defaultdict(list)

        for r in range(len(nums)-1, -1, -1):
            for c in range(len(nums[r])):
                group_id = r + c
                groups[group_id].append(nums[r][c])
        
        cur = 0
        res = []

        while cur in groups:
            res.extend(groups[cur])
            cur += 1

        return res