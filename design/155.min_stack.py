'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        
        
    def push(self, x: int) -> None:
        cur_min = self.getMin()

        if cur_min is None or x < cur_min:
            cur_min = x
        
        self.stk.append((x, cur_min))


    def pop(self) -> None:
        if self.stk:
            self.stk.pop()


    def top(self) -> int:
        return self.stk[-1][0] if self.stk else None


    def getMin(self) -> int:
        return self.stk[-1][1] if self.stk else None
