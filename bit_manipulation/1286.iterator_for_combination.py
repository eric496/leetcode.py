"""
Design an Iterator class, which has:
A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.

Example:
CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.
iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false

Constraints:
1 <= combinationLength <= characters.length <= 15
There will be at most 10^4 function calls per test.
It's guaranteed that all calls of the function next are valid.
"""


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.s = characters
        self.length = len(self.s)
        self.k = combinationLength
        self.mask = (1 << self.length) - 1
        

    def next(self) -> str:
        while self.mask and self.getMaskLength() != self.k:
            self.mask -= 1
            
        res = ""
        
        for i in range(self.length):
            if self.mask & (1 << self.length - i - 1):
                res += self.s[i]
                
        self.mask -= 1
        
        return res

    
    def hasNext(self) -> bool:
        while self.mask and self.getMaskLength() != self.k:
            self.mask -= 1
            
        if self.mask:
            return True
        
        return False
        

    def getMaskLength(self) -> int:
        mask = self.mask
        res = 0
        
        while mask:
            res += mask & 1
            mask >>= 1
        
        return res
        

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
