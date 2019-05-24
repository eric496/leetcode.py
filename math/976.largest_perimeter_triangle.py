"""
Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.
If it is impossible to form any triangle of non-zero area, return 0.

Example 1:
Input: [2,1,2]
Output: 5

Example 2:
Input: [1,2,1]
Output: 0

Example 3:
Input: [3,2,3,4]
Output: 10

Example 4:
Input: [3,6,2,3]
Output: 8
 
Note:
3 <= A.length <= 10000
1 <= A[i] <= 10^6
"""

# Solution 1
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        
        for i in range(len(A)-2):
            if self.can_form_triangle(A[i], A[i+1], A[i+2]):
                return A[i] + A[i+1] + A[i+2]
            
        return 0
        
        
    def can_form_triangle(self, a: int, b: int, c: int) -> bool:
        return a+b > c and a+c > b and b+c > a


# Solution 2: Simplified version - only need to check A[i] < A[i+1] + A[i+2]
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        
        for i in range(len(A)-2):
            if A[i] < A[i+1] + A[i+2]:
                return A[i] + A[i+1] + A[i+2]
            
        return 0
