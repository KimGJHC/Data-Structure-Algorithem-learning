"""
1474. Delete N Nodes After M Nodes of a Linked List
You are given the head of a linked list and two integers m and n.

Traverse the linked list and remove some nodes in the following way:

Start with the head as the current node.
Keep the first m nodes starting with the current node.
Remove the next n nodes
Keep repeating steps 2 and 3 until you reach the end of the list.
Return the head of the modified list after removing the mentioned nodes.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        res = head

        while head.next:
            need = m - 1
            while need > 0 and head.next:
                head = head.next
                need -= 1
            if not head.next:
                break

            delete_start = head.next

            delete = n - 1
            while delete > 0 and delete_start.next:
                delete_start = delete_start.next
                delete -= 1
            if not delete_start.next:
                head.next = None
                break
            head.next = delete_start.next
            head = delete_start.next
        return res