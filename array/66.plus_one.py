'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 1
        
        for d in digits[::-1]:
            res.append((d+carry)%10)
            carry = (d+carry) // 10
        
        if carry:
            res.append(carry)
            
        return res[::-1]

# One liner
class Solution:
    def plusOne(self, digits: list) -> list:
        return [int(d) for d in list(str(int(''.join(map(str, digits))) + 1))]