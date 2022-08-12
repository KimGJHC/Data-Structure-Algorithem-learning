"""
1530. Number of Good Leaf Nodes Pairs

You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countPairs(self, root, distance):
        self.distance = distance
        self.good_pair_count = 0

        def postorder(node):
            # return {} where key is the distance of node to leaves and value is number of such leaves
            if not node:
                return {}

            left = postorder(node.left)
            right = postorder(node.right)

            if not left and not right:
                return {0: 1}
            elif not right:
                return {key + 1: left[key] for key in left}
            elif not left:
                return {key + 1: right[key] for key in right}
            else:
                for left_distance in left:
                    for right_distance in right:
                        if left_distance + right_distance + 2 <= self.distance:
                            self.good_pair_count += left[left_distance] * right[right_distance]

                distanceToLeave = {}

                for key in set(list(left.keys()) + list(right.keys())):
                    distanceToLeave[key + 1] = left.get(key, 0) + right.get(key, 0)
                return distanceToLeave

        postorder(root)

        return self.good_pair_count

# solution 1: postorder
# time: O(n ** 2)
# space: O(h)

    def countPairs(self, root, distance):
        count = 0

        def dfs(node):
            nonlocal count
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            left = dfs(node.left)
            right = dfs(node.right)
            count += sum(l + r <= distance for l in left for r in right)
            return [n + 1 for n in left + right if n + 1 < distance]

        dfs(root)
        return count

# solution 2: similar idea with return of array