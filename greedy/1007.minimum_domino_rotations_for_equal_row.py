"""
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
We may rotate the i-th domino, so that A[i] and B[i] swap values.
Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.
If it cannot be done, return -1.

Example 1:
Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

Example 2:
Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.

Note:
1 <= A[i], B[i] <= 6
2 <= A.length == B.length <= 20000
"""


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        # Case 1: A is the equal row with swapping the first values
        cnt1 = self.swap(A, B, B[0])
        # Case 2: A is the equal row without swapping the first values
        cnt2 = self.swap(A, B, A[0])
        # Case 3: B is the equal row with swapping the first values
        cnt3 = self.swap(B, A, A[0])
        # Case 4: B is the equal row without swapping the first values
        cnt4 = self.swap(B, A, B[0])

        res = min(cnt1, cnt2, cnt3, cnt4)

        return res if res != 20001 else -1

    def swap(self, A: List[int], B: List[int], common: int) -> int:
        cnt = 0

        for a, b in zip(A, B):
            # Do not forget a != common, if a == common, no need to swap
            if b == common and a != common:
                cnt += 1
            elif a != common:
                return 20001

        return cnt
