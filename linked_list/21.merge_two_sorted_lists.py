'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

'''
Thought:
    1. Use a sentinel node to track the head of the result list;
       Use a walking pointer to build the result linked list by appending new list node.
    2. Traverse l1 and l2, comparing node values from the two list nodes. Append the smaller one to the result list. 
    3. l1 and l2 are possible of different length. 
       In this case, append what is left in the longer linked list to the result list.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# Solution 1: Recursive
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if None in (l1, l2):
            return l1 or l2
        
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


# Solution 2: Iterative
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Pythonic way to check the empty linked lists
        if None in (l1, l2):
            return l1 or l2

        sentinel = walk = ListNode(-1)

        while l1 and l2:
            if l1.val < l2.val:
                walk.next = l1
                l1 = l1.next
            else:
                walk.next = l2
                l2 = l2.next

            # Remember to move walking pointer forward 
            walk = walk.next

        # This is Pythonic! 
        walk.next = l1 or l2
        # Compare to the following
        # if l1:
        #     walk.next = l1
        # if l2:
        #     walk.next = l2

        return sentinel.next
