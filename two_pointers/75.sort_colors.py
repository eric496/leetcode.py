"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""


"""
Thought Process:
    1. Partition into 4 zones with 3 pointers: Maintain `low` (boundary for 0s),
       `mid` (current scanner), and `high` (boundary for 2s).
    2. Loop invariant:
       - `nums[0 : low]` contains only 0s.
       - `nums[low : mid]` contains only 1s.
       - `nums[mid : high + 1]` is unprocessed.
       - `nums[high + 1 : n]` contains only 2s.
    3. Handle `nums[mid] == 0`: Swap with `nums[low]` and advance both `low`
       and `mid` (the swapped-in value at `low` is guaranteed to be 1 or 0).
    4. Handle `nums[mid] == 1`: Already in the middle zone; advance `mid` only.
    5. Handle `nums[mid] == 2`: Swap with `nums[high]` and decrement `high`
       only; keep `mid` stationary to inspect the unknown swapped-in element.
    6. Terminate at `mid > high`: The unprocessed region is empty.

Complexity:
    Time: O(n) — single pass; every iteration increments `mid` or decrements `high`.
    Space: O(1) — in-place swaps with three integer pointers.
"""


# Solution 1: counting sort
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = [0] * 3

        for n in nums:
            cnt[n] += 1

        c0, c1, c2 = cnt

        for i in range(c0):
            nums[i] = 0

        for i in range(c0, c0 + c1):
            nums[i] = 1

        for i in range(c0 + c1, c0 + c1 + c2):
            nums[i] = 2


# Solution 2: Dutch National Flag problem (https://en.wikipedia.org/wiki/Dutch_national_flag_problem)
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
