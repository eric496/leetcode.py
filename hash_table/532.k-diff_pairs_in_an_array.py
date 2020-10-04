"""
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

Note:
The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].
"""


# Solution 1: hashmap
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        cnt, res = {}, 0

        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1

        for num in cnt:
            if k > 0 and num + k in cnt:
                res += 1
            elif k == 0 and cnt[num] > 1:
                res += 1

        return res


# Solution 2: two pointers
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return 0
        
        nums.sort()
        i = j = 0
        res = 0
        n = len(nums)
        
        while i < n and j < n:
            if i == j or nums[i] + k > nums[j]:
                j += 1
            elif nums[i] + k < nums[j]:
                i += 1
            else:
                res += 1
                i += 1
                
                while j < n - 1 and nums[j] == nums[j+1]:
                    j += 1
                    
                j += 1
            
        return res
        