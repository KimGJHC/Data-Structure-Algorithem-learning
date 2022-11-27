"""
2487. Remove Nodes From Linked List
You are given the head of a linked list.

Remove every node which has a node with a strictly greater value anywhere to the right side of it.

Return the head of the modified linked list.

# reverse list
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse_head = self.reverse(head)

        prev = reverse_head
        maxx = prev.val
        current = reverse_head.next

        while current:
            if current.val < maxx:
                prev.next = current.next
                current = current.next
            else:
                maxx = current.val
                prev = current
                current = current.next

        res = self.reverse(reverse_head)
        return res

    def reverse(self, head):
        prev = None
        current = head

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev