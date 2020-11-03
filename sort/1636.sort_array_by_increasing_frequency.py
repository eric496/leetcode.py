"""
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.
Return the sorted array.

Example 1:
Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

Example 2:
Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.

Example 3:
Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]

Constraints:
1 <= nums.length <= 100
-100 <= nums[i] <= 100
"""


# Solution 1
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = {}
        
        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1
            
        arr = [(freq, num) for num, freq in cnt.items()]
        arr.sort(key=lambda x: (x[0], -x[1]))
        res = []
        
        for freq, num in arr:
            res += [num] * freq
            
        return res


# Solution 2: simplified
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = {}
        
        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1
            
        return sorted(nums, key=lambda x: (cnt[x], -x))
        