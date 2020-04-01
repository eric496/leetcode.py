"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:
Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Note: 
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
"""


# Brute force solution: O(n^2) TC and O(1) SC
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        res = []
        
        for i in range(len(nums)-k+1):
            res.append(max(nums[i:i+k]))
            
        return res


# Solution 2: Heap: O(Nlogk) TC and O(n) SC
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = []
        res = []
        
        for i,n in enumerate(nums):
            if i+1 < k:
                heapq.heappush(pq, (-n, i))
            else:
                heapq.heappush(pq, (-n, i))
                x, idx = self.find_max(pq, i-k+1)
                res.append(-x)
                heapq.heappush(pq, (x, idx))
                
        return res
                
                
    def find_max(self, pq: List[int], start: int) -> tuple:
        while True:
            x, idx = heapq.heappop(pq)
            
            if idx >= start:
                return x, idx


# Solution 3: O(n) TC and O(n) SC using deque
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k < 1:
            return []
        
        window = deque()
        res = []
        
        for i in range(len(nums)):
            if i >= k and window[0] <= i-k:
                window.popleft()
            
            while window and nums[window[-1]] <= nums[i]:
                window.pop()
                
            window.append(i)
            
            if i >= k-1:
                res.append(nums[window[0]])
            
        return res
        