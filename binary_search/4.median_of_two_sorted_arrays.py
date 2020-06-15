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

# Solution 1: merge sort - O(m + n) TC and O(m + n) SC
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        res = self.merge(nums1, nums2)

        if (m + n) & 1:
            return res[m + n >> 1]
        else:
            return (res[(m + n >> 1) - 1] + res[m + n >> 1]) / 2

    def merge(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [0] * (len(nums1) + len(nums2))
        i = j = k = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                res[k] = nums1[i]
                i += 1
            else:
                res[k] = nums2[j]
                j += 1

            k += 1

        while i < len(nums1):
            res[k] = nums1[i]
            i += 1
            k += 1

        while j < len(nums2):
            res[k] = nums2[j]
            j += 1
            k += 1

        return res


# Solution 2: binary search O(log(m + n))
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)

        low, high = 0, m

        while low <= high:
            partition1 = low + (high - low >> 1)
            partition2 = (m + n + 1 >> 1) - partition1

            max_left1 = float("-inf") if partition1 == 0 else nums1[partition1 - 1]
            min_right1 = float("inf") if partition1 == m else nums1[partition1]
            max_left2 = float("-inf") if partition2 == 0 else nums2[partition2 - 1]
            min_right2 = float("inf") if partition2 == n else nums2[partition2]

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if (m + n) & 1:
                    return float(max(max_left1, max_left2))
                else:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
            elif max_left1 > min_right2:
                high = partition1 - 1
            else:
                low = partition1 + 1
