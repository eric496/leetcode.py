"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3
[2,3], the median is (2 + 3) / 2 = 2.5
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note:
You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.
Answers within 10^-5 of the actual value will be accepted as correct.
"""


import heapq
from collections import defaultdict


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if not nums:
            return []
        
        minh = []
        maxh = []
        
        for i in range(k):
            if len(minh) == len(maxh):
                heapq.heappush(minh, -heapq.heappushpop(maxh, -nums[i]))
            else:
                heapq.heappush(maxh, -heapq.heappushpop(minh, nums[i]))
                
        res = [float(minh[0]) if k&1 else (minh[0] - maxh[0]) / 2]
        delete = defaultdict(int)
        
        for i in range(k, len(nums)):
            heapq.heappush(maxh, -heapq.heappushpop(minh, nums[i]))
            out = nums[i-k]
            
            if out > -maxh[0]:
                heapq.heappush(minh, -heapq.heappop(maxh))
                
            delete[out] += 1
            
            while maxh and delete[-maxh[0]]:
                delete[-maxh[0]] -= 1
                heapq.heappop(maxh)
                
            while minh and delete[minh[0]]:
                delete[minh[0]] -= 1
                heapq.heappop(minh)
                
            res.append(float(minh[0]) if k&1 else (minh[0] - maxh[0]) / 2)
            
        return res
        