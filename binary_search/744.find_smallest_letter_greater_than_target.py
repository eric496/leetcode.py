"""
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.
Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"

Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.
"""


# Solution 1
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if ord(target) >= ord(letters[-1]):
            return letters[0]

        low, high = 0, len(letters) - 1

        while low < high:
            mid = low + ((high - low) >> 2)
            if ord(letters[mid]) <= ord(target):
                low = mid + 1
            else:
                high = mid

        return letters[high]


# Solution 2: optimized
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low, high = 0, len(letters)

        while low < high:
            mid = low + ((high - low) >> 1)

            if ord(letters[mid]) > ord(target):
                high = mid
            else:
                low = mid + 1

        return letters[low % len(letters)]
