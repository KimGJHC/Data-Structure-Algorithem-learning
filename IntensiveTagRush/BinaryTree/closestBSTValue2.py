"""
272. Closest Binary Search Tree Value II

Given the root of a binary search tree, a target value, and an integer k, return the k values in the BST that are closest to the target. You may return the answer in any order.

You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
"""

import heapq
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestKValues(self, root, target, k):
        # use dfs and maintain a heap

        stack = [root]
        heap = []  # stores (-abs(target - nodeVal), nodeVal)

        while stack:
            node = stack.pop()
            node_target_diff = abs(target - node.val)
            if len(heap) < k:
                heapq.heappush(heap, (-node_target_diff, node.val))
            else:
                heapq.heappushpop(heap, (-node_target_diff, node.val))

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)
        return [val for _, val in heap]

# solution 1: use heap + DFS
# time: O(n*log(k)) where n is the size of the tree, k is the size of the heap
# space: O(h+k) where h is the height of the tree


# solution 2: Inorder + Deque
# with the property of BST, imagine deque as sliding window on the inorder traversal of the BST
    def closestKValues_v2(self, root, target, k):
        def inorder(queue, node, target, k):
            if not node:
                return

            inorder(queue, node.left, target, k)

            if len(queue) == k:
                if abs(queue[0] - target) > abs(node.val - target):
                    queue.popleft()
                    queue.append(node.val)
                else:
                    # early stop
                    return
            else:
                queue.append(node.val)

            inorder(queue, node.right, target, k)

        queue = collections.deque()
        inorder(queue, root, target, k)
        return list(queue)

# time: O(n)
# space: O(k)
