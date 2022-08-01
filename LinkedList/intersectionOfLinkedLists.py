"""
160. Intersection of Two Linked Lists
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.
"""

# If we use a hashmap to store the nodes of headA and check if nodes in headB appear in the hashmap
# space will be O(max(n_A, n_B))

# we will use pointers to reduce the space to O(1) while maintain the time complexity at O(n_A + n_B)

def getIntersectionNode(self, headA, headB):
    n_A = 0
    n_B = 0

    tempA = headA
    while tempA:
        n_A += 1
        tempA = tempA.next

    tempB = headB
    while tempB:
        n_B += 1
        tempB = tempB.next

    if n_A > n_B:
        headA, headB = headB, headA
        n_A, n_B = n_B, n_A

    for i in range(n_B - n_A):
        headB = headB.next

    while headA and headA != headB:
        headA = headA.next
        headB = headB.next
    return headA

