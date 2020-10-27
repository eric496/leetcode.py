"""
You are given two strings a and b of the same length. Choose an index and split both strings at the same index, splitting a into two strings: aprefix and asuffix where a = aprefix + asuffix, and splitting b into two strings: bprefix and bsuffix where b = bprefix + bsuffix. Check if aprefix + bsuffix or bprefix + asuffix forms a palindrome.
When you split a string s into sprefix and ssuffix, either ssuffix or sprefix is allowed to be empty. For example, if s = "abc", then "" + "abc", "a" + "bc", "ab" + "c" , and "abc" + "" are valid splits.
Return true if it is possible to form a palindrome string, otherwise return false.
Notice that x + y denotes the concatenation of strings x and y.

Example 1:
Input: a = "x", b = "y"
Output: true
Explaination: If either a or b are palindromes the answer is true since you can split in the following way:
aprefix = "", asuffix = "x"
bprefix = "", bsuffix = "y"
Then, aprefix + bsuffix = "" + "y" = "y", which is a palindrome.

Example 2:
Input: a = "abdef", b = "fecab"
Output: true

Example 3:
Input: a = "ulacfd", b = "jizalu"
Output: true
Explaination: Split them at index 3:
aprefix = "ula", asuffix = "cfd"
bprefix = "jiz", bsuffix = "alu"
Then, aprefix + bsuffix = "ula" + "alu" = "ulaalu", which is a palindrome.

Example 4:
Input: a = "xbdef", b = "xecab"
Output: false

Constraints:
1 <= a.length, b.length <= 105
a.length == b.length
a and b consist of lowercase English letters
"""


class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return self.validate(a, b) or self.validate(b, a)
        
    def validate(self, a: str, b: str) -> bool:
        left, right = 0, len(a) - 1
        
        while left < right:
            if a[left] != b[right]:
                break
            
            left += 1
            right -= 1
            
        return self.isPalindrome(a, left, right) or self.isPalindrome(b, left, right)  
        
    def isPalindrome(self, s: str, left: int, right: int) -> bool: 
        while left < right:
            if s[left] != s[right]:
                 return False
            
            left += 1
            right -= 1
            
        return True
        