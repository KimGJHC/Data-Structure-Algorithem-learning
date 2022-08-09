"""
863. All Nodes Distance K in Binary Tree

Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.
"""

import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root, target, k: int):
        def dfs(node, parent=None):
            if node:
                node.parent = parent
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        # bfs
        queue = collections.deque([target])
        visited = set()
        for i in range(k):
            queue_length = len(queue)
            for _ in range(queue_length):
                node = queue.popleft()
                visited.add(node)

                for neighbor in (node.left, node.right, node.parent):
                    if neighbor and neighbor not in visited:
                        queue.append(neighbor)

        return [node.val for node in queue]

# solution 1: convert tree to graph + BFS
# time: O(n) where n is the size of tree
# space: O(n)
    def distanceK_v2(self, root, target, k):
        res = []

        def subtree_add(node, distance):
            # add all nodes with k - distance from target
            if not node:
                return
            elif distance == k:
                res.append(node.val)
            elif distance < k:
                subtree_add(node.left, distance+1)
                subtree_add(node.right, distance+1)
            else:
                return

        def postorder(node):
            if not node:
                return -1
            elif node == target:
                subtree_add(node, 0)
                return 1
            else:
                left, right = postorder(node.left), postorder(node.right)
                if left != -1:
                    if left == k:
                        res.append(node.val)
                    subtree_add(node.right, left + 1)
                    return left + 1
                elif right != -1:
                    if right == k:
                        res.append(node.val)
                    subtree_add(node.left, right + 1)
                    return right + 1
                else:
                    return -1

        postorder(root)

        return res

# time: O(n)
# space: O(n)