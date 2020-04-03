"""
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.

Note: The length of given array won't exceed 10000.
"""


# Solution: forward traversal
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nxt = {i: -1 for i in range(len(nums))}
        stk = []
        nums2 = nums * 2

        for i, n in enumerate(nums2):
            while stk and nums[stk[-1]] < n:
                nxt[stk.pop()] = n

            if i < len(nums):
                stk.append(i)

        return [nxt[i] for i in range(len(nums))]


# Solution: backward traversal
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stk = []
        res = [-1] * n

        for i in range(2 * n - 1, -1, -1):
            num = nums[i % n]

            while stk and stk[-1] <= num:
                stk.pop()

            res[i % n] = stk[-1] if stk else -1
            stk.append(num)

        return res
