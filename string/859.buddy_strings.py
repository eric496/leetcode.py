"""
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

Example 1:
Input: A = "ab", B = "ba"
Output: true

Example 2:
Input: A = "ab", B = "ab"
Output: false

Example 3:
Input: A = "aa", B = "aa"
Output: true

Example 4:
Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true

Example 5:
Input: A = "", B = "aa"
Output: false

Note:
0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.
"""

"""
Thought process:
    1. If length of A and B are different then they are not buddies. 
    2. If A and B are identical, and A contains duplicate letters, then we can swap the duplicates and they are buddies, e.g. A = 'aa', b = 'aa'.
    3. Store all different letter pairs, if their are extactly two pairs and they are reversed to each other, then they are buddies, 
       e.g. A = 'ab', B = 'ba' => diff = [('a', 'b'), ('b', 'a')] => ('a', 'b') is reversed ('b', 'a') => they are buddies.
            A = 'aa', B = 'cc' => diff = [('a', 'c'), ('a', 'c')] => though length of diff is 2, but the pairs are not reversed equivalent to each other => they are not buddies.
"""

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        
        if A == B and len(set(A)) < len(A):
            return True
        
        diff = [(a,b) for a,b in zip(A,B) if a != b]
        
        return len(diff) == 2 and diff[0] == diff[1][::-1]
