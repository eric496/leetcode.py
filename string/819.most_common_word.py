'''
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

Example:

Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
 

Note:

1 <= paragraph.length <= 1000.
1 <= banned.length <= 100.
1 <= banned[i].length <= 10.
The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
There are no hyphens or hyphenated words.
Words only consist of letters, never apostrophes or other punctuation symbols.
'''

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list) -> str:
        ignore_ch = set("!?',;.")

        # Replace ignored characters with space instead of "", because there is such case "a, b,b,b,b, c"
        # You don't want to convert it to "a bbbb c", but "a b b b b c" instead
        for ch in ignore_ch:
            paragraph = paragraph.replace(ch, ' ')
        
        words = paragraph.lower().split()
        freq = {}
        most_common = None
        max_freq = 0
        
        for w in words:
            if w not in banned:
                freq[w] = freq.get(w, 0) + 1
                
                if freq[w] > max_freq:
                    max_freq = freq[w]
                    most_common = w
            
        return most_common