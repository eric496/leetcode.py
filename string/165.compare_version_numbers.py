"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.
You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.
You may assume the default revision number for each level of a version number to be 0. For example, version number 3.4 has a revision number of 3 and 4 for its first and second level revision number. Its third and fourth level revision number are both 0.

Example 1:
Input: version1 = "0.1", version2 = "1.1"
Output: -1

Example 2:
Input: version1 = "1.0.1", version2 = "1"
Output: 1

Example 3:
Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1

Example 4:
Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both “01” and “001" represent the same number “1”

Example 5:
Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: The first version number does not have a third level revision number, which means its third level revision number is default to "0"

Note:
Version strings are composed of numeric strings separated by dots . and this numeric strings may have leading zeroes.
Version strings do not start or end with dots, and they will not be two consecutive dots.
"""


# Solution 1: Pad trailing zeros
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(d) for d in version1.split(".")]
        v2 = [int(d) for d in version2.split(".")]
        n1, n2= len(v1), len(v2)

        if n1 > n2:
            v2 += [0] * (n1 - n2)

        if n2 > n1:
            v1 += [0] * (n2 - n1)

        for d1, d2 in zip(v1, v2):
            if d1 > d2:
                return 1
            elif d1 < d2:
                return -1

        return 0


# Solution 2
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        i = j = 0
        n1, n2 = len(v1), len(v2)

        while i < n1 and j < n2:
            if int(v1[i]) < int(v2[j]):
                return -1

            if int(v1[i]) > int(v2[j]):
                return 1

            i += 1
            j += 1

        while i < n1:
            if int(v1[i]):
                return 1

            i += 1

        while j < n2:
            if int(v2[j]):
                return -1

            j += 1

        return 0
