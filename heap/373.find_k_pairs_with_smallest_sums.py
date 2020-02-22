"""
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
Define a pair (u,v) which consists of one element from the first array and one element from the second array.
Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]] 
Explanation: The first 3 pairs are returned from the sequence: 
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:
Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence: 
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Example 3:
Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
"""


# Solution 1: Brute force O(n^2)
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        
        for n1 in nums1:
            for n2 in nums2:
                res.append([n1, n2])
                
        res.sort(key=lambda x: sum(x))
        
        return res[:k]


# Solution 2: Heap
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        res, hp = [], []
        
        for i in range(len(nums1)):
            heapq.heappush(hp, (nums1[i]+nums2[0], i, 0))
        
        while hp and k:
            _, i, j = heapq.heappop(hp)
            res.append([nums1[i], nums2[j]])
            if j+1 < len(nums2):
                heapq.heappush(hp, (nums1[i]+nums2[j+1], i, j+1))
            k -= 1
        
        return res
