"""
328. Odd Even Linked List
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.
"""


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        even_head = head.next

        odd = head
        even = even_head

        i = 1  # take next to be odd if 1 else even
        while True:
            if i == 1:
                if not even.next:
                    odd.next = None
                    break
                odd.next = even.next
                odd = odd.next
            else:
                if not odd.next:
                    even.next = None
                    break
                even.next = odd.next
                even = even.next
            i *= -1
        odd.next = even_head
        return head