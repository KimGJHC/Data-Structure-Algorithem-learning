"""
86. Partition List
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

# consider 2 pointers, design pop and insert operations, define conditions so that left pointer does not surpass right pointer
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(-float('inf'))
        dummy.next = head
        left, right = dummy, dummy

        while right is not None and right.next is not None:
            if right.next.val >= x:
                right = right.next
            elif left.next.val < x and left != right:
                left = left.next
            elif left != right:
                node = self.popNext(right)
                self.insertNext(left, node)
            else:
                left = left.next
                right = right.next
        return dummy.next

    def popNext(self, node):
        # pop node.next and connect node to node.next.next
        if node.next is None:
            return None

        res = node.next
        node.next = res.next
        return res

    def insertNext(self, prev, node):
        # insert node to prev.next
        node.next = prev.next
        prev.next = node
        return