"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:
Input:  [1,2,1,3,2,5]
Output: [3,5]

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""


# Solution 1: use hashmap - O(n) TC and O(n) SC
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        cnt = {}

        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1

        return [k for k, v in cnt.items() if v == 1]


# Solution 2: bit manipulation
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0

        for num in nums:
            xor ^= num

        last_set_bit = xor & ~xor + 1
        res = [0, 0]

        for num in nums:
            if num & last_set_bit:
                res[0] ^= num
            else:
                res[1] ^= num

        return res
