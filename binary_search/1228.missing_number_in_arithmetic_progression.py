"""
In some array arr, the values were in arithmetic progression: the values arr[i+1] - arr[i] are all equal for every 0 <= i < arr.length - 1.
Then, a value from arr was removed that was not the first or last value in the array.
Return the removed value.

Example 1:
Input: arr = [5,7,11,13]
Output: 9
Explanation: The previous array was [5,7,9,11,13].

Example 2:
Input: arr = [15,13,12]
Output: 14
Explanation: The previous array was [15,14,13,12].

Constraints:
3 <= arr.length <= 1000
0 <= arr[i] <= 10^5
"""


# Solution 1: O(n) TC
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        diff = 0
        
        for i in range(len(arr)-1):
            d = arr[i+1] - arr[i]
            if diff * 2 == d:
                return arr[i] + diff
            diff = d
            
        return arr[0] + diff


# Solution 2: Binary Search
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        diff = (arr[-1]-arr[0]) // len(arr)
        low, high = 0, len(arr)
        
        while low < high:
            mid = (low+high) >> 1
            if arr[mid] == arr[0] + diff*mid:
                low = mid + 1
            else:
                high = mid
            
        return arr[0] + low*diff
        