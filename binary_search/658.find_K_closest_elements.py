"""
Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]

Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
"""


# Solution: look at (k+1) range and remove left or right end element
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low, high = 0, len(arr) - k

        while low < high:
            mid = low + ((high - low) >> 1)

            if x - arr[mid] > arr[mid + k] - x:
                low = mid + 1
            else:
                high = mid

        return arr[low : low + k]
