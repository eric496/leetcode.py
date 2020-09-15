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
                Since looking up values in set takes constant time, the time complexity is thus O(n), the space time complexity is O(n).

    Follow up : Floyd's algorithm for cycle detection.
                Find graph explanations here: https://stackoverflow.com/questions/2936213/explain-how-finding-cycle-start-node-in-cycle-linked-list-work
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Solution 1: Use a set
# Time complexity: O(n)
# Space complexity: O(n)
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


# Follow up: Floyd's algorithm for cycle detection
# Time complexity: O(n)
# Space complexity: O(1)
class Solution(object):
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                break

        # If there is cycle, fast and fast.next should not be null
        if fast and fast.next:
            slow = head

            while slow is not fast:
                slow = slow.next
                fast = fast.next

            return slow
        # There is no cycle
        else:
            return None


# A variation
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                break
        else:
            return None

        slow = head

        while slow is not fast:
            slow = slow.next
            fast = fast.next

        return slow


# Solution 3: Notice the location of if statement in the while loops 
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # Move pointers and then check equality
            if slow is fast:
                break
        
        if not fast or not fast.next:
            return None
        
        slow = head
        
        while slow:
            # Check equality first and then move pointers
            if slow is fast:
                return slow
            
            slow = slow.next 
            fast = fast.next
            
        return None
