"""
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.
Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.
"""

# Definition for a Node.
class ListNode:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


# Solution 1
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
         
        cur = head
        
        while cur:
            if not cur.child:
                cur = cur.next
                continue 
                
            child_cur = cur.child

            while child_cur.next:
                child_cur = child_cur.next

            child_cur.next = cur.next

            if cur.next:
                cur.next.prev = child_cur

            cur.next = cur.child
            cur.child.prev = cur
            cur.child = None
            
        return head


# Solution 2: DFS
class Solution:
    def flatten(self, head: ListNode) -> ListNode:
        walk = head

        while walk:
            if walk.child:
                nxt = walk.next
                walk.next = self.flatten(walk.child)
                walk.next.prev = walk
                walk.child = None

                while walk.next:
                    walk = walk.next

                if nxt:
                    walk.next = nxt
                    walk.next.prev = walk

            walk = walk.next

        return head


# Solution 3: Stack
class Solution:
    def flatten(self, head: ListNode) -> ListNode:
        if not head:
            return head

        sentinel = prev = ListNode(None, None, head, None)
        stk = [head]

        while stk:
            cur = stk.pop()
            cur.prev = prev
            prev.next = cur
            prev = cur

            if cur.next:
                stk.append(cur.next)
                cur.next = None

            if cur.child:
                stk.append(cur.child)
                cur.child = None

        sentinel.next.prev = None

        return sentinel.next
