"""
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.
Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.
"""

# Solution 1:
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq, cnt, res = {}, {n: 1 for n in range(1, len(nums) + 1)}, []

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
            if freq[n] > 1:
                res.append(n)
            cnt[n] -= 1

        for k in cnt:
            if cnt[k] == 1:
                res.append(k)
                break

        return res


# Solution 2: more concise
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = [0] * (len(nums) + 1)
        dup = missing = -1

        for n in nums:
            freq[n] += 1

        for n in range(1, len(nums) + 1):
            if freq[n] == 2:
                dup = n

            if freq[n] == 0:
                missing = n

        return [dup, missing]
