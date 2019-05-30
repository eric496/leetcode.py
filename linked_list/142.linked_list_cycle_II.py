"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
Note: Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Follow up:
Can you solve it without using extra space?
"""

"""
Thought process:
    Solution 1: Use a set to track all visited nodes, once we find an already visited node, it is the entry node of the cycle.
                Since `in` operation for set in constant time, time complexity is O(n).

    Solution 2: Floyd's algorithm for cycle detection.
                Find graph explanations here: https://stackoverflow.com/questions/2936213/explain-how-finding-cycle-start-node-in-cycle-linked-list-work
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Solution 1: Use a set
# O(n) TC; O(n) SC
class Solution(object):
    def detectCycle(self, head: ListNode) -> ListNode:
        seen = set()
        walk = head
        
        while walk:
            if walk in seen: 
                return walk
            else:
                seen.add(walk)

            walk = walk.next
            
        return None


# Solution 2: Floyd's algorithm for cycle detection
# O(n) TC; O(1) SC
class Solution(object):
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                break
        
        # If there is cycle, fast and fast.next should not be null
        if fast and fast.next:
            slow = head
            while slow is not fast:
                slow, fast = slow.next, fast.next
            return slow
        # There is no cycle
        else:
            return None
