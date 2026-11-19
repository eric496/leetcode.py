"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""


"""
Thought Process:
    1. Avoid division: Division fails on zeroes and is forbidden by
       the problem constraints.
    2. Split around index i: Every `res[i]` equals
       `(product of elements left of i) * (product of elements right of i)`.
    3. Forward pass (prefixes): Fill `res[i]` with the running
       product of all elements strictly before index `i` (seeded with `1`
       at index `0`).
    4. Backward pass (suffixes): Maintain a single `suffix` variable
       (seeded with `1`) from right to left, multiplying `res[i]`
       by `suffix_prod` before updating `suffix_prod *= nums[i]`.
    5. Reuse output array: Storing prefixes directly in `res` eliminates
       extra prefix_prod/suffix_prod arrays, achieving O(1) auxiliary space.

Complexity:
    Time: O(n)
    Space: O(1) extra space (excluding the output array)
"""


# Solution 1: O(n) TC and O(n) SC
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        res = []

        for i in range(n):
            res.append(left[i] * right[i])

        return res


# Follow up: O(n) TC and O(1) SC
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n

        prefix_prod = 1
        for left in range(n):
            res[left] *= prefix_prod
            prefix_prod *= nums[left]
        
        suffix_prod = 1
        for right in range(n - 1, -1, -1):
            res[right] *=  suffix_prod
            suffix_prod *= nums[right]

        return res
