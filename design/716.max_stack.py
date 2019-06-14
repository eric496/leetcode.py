'''
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.

Example 1:
MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5

Note:
-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.
'''

"""
Thought process:
    Use two stacks, one to push input elements, one to store the current max value in the stack.
"""

# O(n) TC and O(n) SC
class MaxStack:

    def __init__(self):
        self.stk = []
        self.max_stk = []
        

    def push(self, x: int) -> None:
        self.stk.append(x)
        
        if self.max_stk:
            self.max_stk.append(max(x, self.max_stk[-1]))
        else:
            self.max_stk.append(x)
        
        
    def pop(self) -> int:
        self.max_stk.pop()
        return self.stk.pop()
        
        
    def top(self) -> int:
        return self.stk[-1]
        

    def peekMax(self) -> int:
        return self.max_stk[-1]
        

    def popMax(self) -> int:
        cur_max = self.peekMax()
        temp = []
        
        while self.stk[-1] != cur_max:
            temp.append(self.stk.pop())
            self.max_stk.pop()
        
        self.stk.pop()
        self.max_stk.pop()
        
        while temp:
            self.push(temp.pop())
        
        return cur_max
        