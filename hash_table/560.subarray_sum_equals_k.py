"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2

Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""


"""
Thought Process:
    1. Rule out sliding window: Negative numbers break monotonicity, so
       shrinking a window cannot reliably shrink the sum.
    2. Express any subarray as a difference: Every subarray sum equals
       `current_sum - previous_prefix_sum`.
    3. Rearrange the equation: Setting
       `current_sum - previous_prefix_sum = k` gives
       `previous_prefix_sum = current_sum - k`.
    4. Count valid cut points with a hash map: Track how many times
       each prefix sum has appeared so far.
    5. Seed `{0: 1}` before starting: Account for subarrays that start
       directly at index 0 without chopping off a prefix.
    6. Accumulate in one pass: At each element, add
       `prefix_counts[current_sum - k]` to the answer, then record
       `current_sum`.
    
    Complexity:
        Time: O(n)
        Space: O(n)
"""


from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_sum = 0
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1
        count = 0

        for num in nums:
            current_sum += num
            count += prefix_counts[current_sum - k]
            prefix_counts[current_sum] += 1

        return count
