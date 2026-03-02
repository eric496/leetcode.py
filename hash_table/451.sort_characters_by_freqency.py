"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:
Input:
"tree"
Output:
"eert"
Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input:
"cccaaa"
Output:
"cccaaa"
Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input:
"Aabb"
Output:
"bbAa"
Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""


# Solution 1: hash table
from collections import defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        count = defaultdict(int)

        for c in s:
            count[c] += 1
        
        freq_list = [(freq, char) for char, freq in count.items()]
        freq_list.sort(reverse=True)

        return "".join(char*freq for freq, char in freq_list)



# Solution 2: bucket sort
from collections import defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        count = defaultdict(int)

        for c in s:
            count[c] += 1
        
        bucket = defaultdict(list)

        for char, freq in count.items():
            bucket[freq].append(char)

        res = []
        for freq in range(len(s), 0, -1):
            if freq in bucket:
                for char in bucket[freq]:
                    res.append(char * freq)
        
        return "".join(res)
    