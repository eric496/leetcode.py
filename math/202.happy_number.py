'''
Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        while True:
            sum_of_squares = 0
            while n != 0:
                sum_of_squares += (n%10) ** 2
                n //= 10
            if sum_of_squares == 1:
                return True
            elif sum_of_squares in nums:
                return False
            else:
                nums.add(sum_of_squares)
            n = sum_of_squares   

# a more concise and smart pythonic solution
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            n = sum([int(ch) ** 2 for ch in str(n)])
            if n in seen:
                return False
            else:
                seen.add(n)
        return True