"""
An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
     ↓
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
     ↓   ↓    ↓    ↓  ↓    
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
     ↓   ↓    ↓
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example:
Given dictionary = [ "deer", "door", "cake", "card" ]
isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true
"""


class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.d = {}
        
        for word in dictionary:
            key = self.abbr(word)
            if key in self.d:
                self.d[key].add(word)
            else:
                self.d[key] = {word}
        
        
    def isUnique(self, word: str) -> bool:
        key = self.abbr(word)
        return True if key not in self.d or self.d[key] == {word} else False
        
        
    def abbr(self, word):
        return word if len(word)<3 else word[0]+str(len(word)-2)+word[-1]
        