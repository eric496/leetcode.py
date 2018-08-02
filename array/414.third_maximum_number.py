'''
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''

class Solution:
    def thirdMax(self, nums: list) -> int:
        max3 = [float('-inf')] * 3
        for num in nums:
            if num not in max3:
                if num > max3[0]:
                    max3 = [num, max3[0], max3[1]]
                elif num > max3[1]:
                    max3 = [max3[0], num, max3[1]]
                elif num > max3[2]:
                    max3 = [max3[0], max3[1], num]
        return max3[0] if float('-inf') in max3 else max3[-1]