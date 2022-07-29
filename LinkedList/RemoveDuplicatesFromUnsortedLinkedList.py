"""
1836. Remove Duplicates From an Unsorted Linked List

Given the head of a linked list, find all the values that appear more than once in the list and delete the nodes that have any of those values.

Return the linked list after the deletions.
"""

# The idea is to do 2 pass, count each value in first pass and delete values with more than 1 appearance in the second pass
# wonder is there is better method or 1 pass method

import collections
def deleteDuplicatesUnsorted(head):
    visited = collections.defaultdict(int)

    start = head

    while start:
        visited[start.val] += 1
        start = start.next

    temp = ListNode()
    temp.next = head
    res = temp

    while temp.next:
        if visited[temp.next.val] > 1:
            temp.next = temp.next.next
        else:
            temp = temp.next
    return res.next

# time: O(n), n is the number of nodes
# space: O(n)