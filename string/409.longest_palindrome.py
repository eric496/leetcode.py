'''
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = [0] * 52
        for char in s:
            count[ord(char)-ord('a')] += 1
        result = odd = 0
        for n in count:
            if n >= 1 and n % 2 == 1:
                result += n-1
                odd = 1
            else:
                result += n
        return result + 1 if odd else result