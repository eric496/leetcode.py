"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.

Example 1:
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

Example 2:
Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.

Note:
The number of nodes in the given list will be between 1 and 100.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Solution 1
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = ListNode(None)
        slow.next = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # If there is even number of nodes, the fast pointer will point to the last node.
        # Since we need to return the second middle node, the slow pointer needs to move one node forward.
        # On the other hand, if there is odd number of nodes, the fast pointer will point to the tail (None).
        if fast:
            slow = slow.next

        return slow


# Solution 1: a variation
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # # Since it is an non-empty list, we can remove the following code
        # if not head or not head.next:
        #     return head

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        return slow


# Solution 2
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = ListNode(None)
        slow.next = fast.next = head

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow.next
