"""
Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.

Example 1:
Input: A = [4,7,9,10], K = 1
Output: 5
Explanation: 
The first missing number is 5.

Example 2:
Input: A = [4,7,9,10], K = 3
Output: 8
Explanation: 
The missing numbers are [5,6,8,...], hence the third missing number is 8.

Example 3:
Input: A = [1,2,4], K = 3
Output: 6
Explanation: 
The missing numbers are [3,5,6,7,...], hence the third missing number is 6.

Note:
1 <= A.length <= 50000
1 <= A[i] <= 1e7
1 <= K <= 1e8
"""


# Solution 1: O(n) TC
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        nums += [float("inf")]
        prev = nums[0]

        for i in range(1, len(nums)):
            missing = nums[i] - nums[i - 1] - 1

            if k - missing <= 0:
                return prev + k

            k -= missing
            prev = nums[i]


# Solution 2: binary search - O(logn) TC
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        lo, hi = 0, len(nums)

        while lo < hi:
            mid = lo + (hi - lo >> 1)

            if nums[mid] >= nums[0] + mid + k:
                hi = mid
            else:
                lo = mid + 1

        return nums[0] + lo + k - 1
