"""
Given a sorted array of integers nums and integer values a, b and c. Apply a quadratic function of the form f(x) = ax2 + bx + c to each element x in the array.
The returned array must be in sorted order.
Expected time complexity: O(n)

Example 1:
Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]

Example 2:
Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]
"""

"""
Thought process:
    1) It is a convex function if a > 0, it is decreasing from both ends to center.
    2) It is a concave function if a < 0, it is increasing from both ends to center.
    3) It is a monotonic function if a = 0, it is always decreasing or increasing.
"""


class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        res = [0] * len(nums)
        start, end = 0, len(nums)-1
        ix = len(nums) - 1 if a >= 0 else 0
        
        while start <= end:
            quad_start = self.calc_quad(a, b, c, nums[start])
            quad_end = self.calc_quad(a, b, c, nums[end])
            if a >= 0:
                if quad_start >= quad_end: 
                    res[ix] = quad_start
                    start += 1
                else:
                    res[ix] = quad_end
                    end -= 1
                ix -= 1
            else:
                if quad_start > quad_end: 
                    res[ix] = quad_end
                    end -= 1
                else:
                    res[ix] = quad_start
                    start += 1
                ix += 1
                
        return res
                
    
    def calc_quad(self, a: int, b: int, c: int, x: int) -> int:
        return a * x**2 + b * x + c
