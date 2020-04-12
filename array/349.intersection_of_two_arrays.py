"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
"""

# Solution 1: brute force - O(mn) TC
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        
        for n1 in nums1:
            for n2 in nums2:
                if n1 == n2:
                    res.add(n1)
                    
        return list(res)


# Solution 2: two pointers, max(O(nlogn), O(mlogm)) TC
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = j = 0
        res = set()
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            
        return list(res)


# Solution 3: binary search - O(nlogm) TC
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        nums2.sort()
        
        for n in nums1:
            if self.binarySearch(nums2, n):
                res.add(n)
                
        return list(res)
        
    def binarySearch(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = low + ((high-low) >> 1)
            
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        
        return False


# Solution 4: two sets - O(m+n) TC
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
