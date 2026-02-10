"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""


# Solution 1: hash map
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt = {}

        for n in nums1:
            cnt[n] = cnt.get(n, 0) + 1

        res = []

        for n in nums2:
            if n in cnt and cnt[n] > 0:
                res.append(n)
                cnt[n] -= 1

        return res
    

# Follow up 1: two pointers
class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        nums1.sort()
        nums2.sort()
        p1 = p2 = 0
        res = []

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return res


"""
Follow up
2. "What if nums1's size is small compared to nums2's size?"
The Hash Map approach is better.
    We specifically hash the smaller array (nums1).
    This minimizes memory usage to O(K), where K is the size of nums1. The size of nums2 doesn't affect memory usage, only runtime.
3. "What if elements of nums2 are stored on disk, and memory is limited?"
This is an External Merge Sort scenario.
    Scenario A (One fits in memory): If nums1 fits in memory, hash it. Then read chunks of nums2 from disk one by one and check against the hash map.
    Scenario B (Neither fits):
        External Sort: Sort both files on disk using external sort (divide into chunks, sort chunks in memory, write to disk, merge sorted chunks).
        Stream Processing: Once sorted, use the Two Pointers approach. You only need to read one element (or small buffer) from each file at a time, making memory usage negligible.
"""