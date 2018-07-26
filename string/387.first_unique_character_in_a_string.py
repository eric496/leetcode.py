'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        char_index_map = {}
        for ix, char in enumerate(s):
            char_index_map[char] = ix if char_index_map.get(char) is None else len(s)
        return min(char_index_map.values()) if min(char_index_map.values()) < len(s) else -1 