"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:
Input: 2
Output: [0,1,1]

Example 2:
Input: 5
Output: [0,1,1,2,1,2]

Follow up:
It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""


"""
Thought process:
    For even numbers, the number of set bits is same if doubling the number,
    e.g. 6 (110) -> 12 (1100) -> 24 (11000)
    For odd numbers, the number of set bits is its integer division by 2 and then add 1,
    e.g. 25 (11001) -> 12 (1100)   
    Because the last bit is always 1 
"""


class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0] * (num + 1)

        for n in range(1, num + 1):
            if n & 1:
                res[n] = res[n >> 1] + 1
            else:
                res[n] = res[n >> 1]

        return res
