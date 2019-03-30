"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""

# Brute force
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        comb = sorted(nums1+nums2)
        if len(comb)%2:
            return comb[len(comb)//2]
        else:
            return (comb[len(comb)//2]+comb[len(comb)//2-1]) / 2


# Binary search O(log(min(m,n)))
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            short = nums1
            long = nums2
        else:
            short = nums2
            long = nums1

        len1, len2 = len(short), len(long)
        total_len = len1 + len2

        start, end = 0, len(short)

        while start <= end:
            mid1 = start + (end-start)//2
            mid2 = (total_len+1)//2 - mid1

            maxleft1 = float('-inf') if not mid1 else short[mid1-1]
            minright1 = float('inf') if mid1==len1 else short[mid1]
            maxleft2 = float('-inf') if not mid2 else long[mid2-1]
            minright2 = float('inf') if mid2==len2 else long[mid2]

            if maxleft1 <= minright2 and maxleft2 <= minright1:
                if total_len % 2:
                    return float(max(maxleft1, maxleft2))
                else:
                    return (max(maxleft1, maxleft2)+min(minright1, minright2)) / 2
            elif maxleft1 > minright2:
                end = mid1 - 1
            else:
                start = mid1 + 1
