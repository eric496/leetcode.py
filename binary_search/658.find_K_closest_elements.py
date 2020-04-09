"""
Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]

Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
"""


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr)-k
        
        while left < right:
            mid = left + ((right-left)>>1)
            
            if x-arr[mid] > arr[mid+k]-x:
                left = mid + 1
            else:
                right = mid
                
        return arr[left:left+k]
    