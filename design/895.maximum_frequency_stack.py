"""
Implement FreqStack, a class which simulates the operation of a stack-like data structure.
FreqStack has two functions:
push(int x), which pushes an integer x onto the stack.
pop(), which removes and returns the most frequent element in the stack.
If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.
 
Example 1:
Input: 
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
Output: [null,null,null,null,null,null,null,5,7,5,4]
Explanation:
After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:
pop() -> returns 5, as 5 is the most frequent.
The stack becomes [5,7,5,7,4].
pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
The stack becomes [5,7,5,4].
pop() -> returns 5.
The stack becomes [5,7,4].
pop() -> returns 4.
The stack becomes [5,7].
 
Note:
Calls to FreqStack.push(int x) will be such that 0 <= x <= 10^9.
It is guaranteed that FreqStack.pop() won't be called if the stack has zero elements.
The total number of FreqStack.push calls will not exceed 10000 in a single test case.
The total number of FreqStack.pop calls will not exceed 10000 in a single test case.
The total number of FreqStack.push and FreqStack.pop calls will not exceed 150000 across all test cases.
"""

from collections import Counter, defaultdict

class FreqStack:

    def __init__(self):
        self.cnt = Counter()
        self.freq = defaultdict(list)
        self.most_freq = 0
        

    def push(self, x: int) -> None:
        self.cnt[x] += 1
        self.freq[self.cnt[x]].append(x)
        self.most_freq = max(self.most_freq, self.cnt[x])
            
        
    def pop(self) -> int:
        top = self.freq[self.most_freq].pop()
        # Update most frequency of most common elements.
        # If the current list is empty, then there is no other elements
        # with the same frequency as the popped element. Thus most_freq should subtract by one.
        if not self.freq[self.most_freq]:
            self.most_freq -= 1
        self.cnt[top] -= 1
        
        return top

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
