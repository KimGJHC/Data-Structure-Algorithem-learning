"""
1339. Maximum Product of Splitted Binary Tree

Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxProduct(self, root):
        sum_of_tree = 0
        self.MOD = 10 ** 9 + 7

        stack = [root]
        while stack:
            current = stack.pop()
            sum_of_tree += current.val
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

        max_product = 0

        def postorder(node):
            nonlocal sum_of_tree
            nonlocal max_product
            # return the sum of subtree rooted at node
            if not node:
                return 0

            left = postorder(node.left)
            right = postorder(node.right)

            break_left = left * (sum_of_tree - left)
            break_right = right * (sum_of_tree - right)

            max_product = max(max_product, break_left, break_right)

            return node.val + left + right

        postorder(root)
        return max_product % self.MOD
# solution 1: 2 pass the tree, 1 pass for sum, 1 pass for best product
# time: O(n)
# space: O(h)

    def maxProduct_v2(self, root):
        all_sums = []

        def tree_sum(subroot):
            nonlocal all_sums
            if not subroot:
                return 0
            left_sum = tree_sum(subroot.left)
            right_sum = tree_sum(subroot.right)
            total_sum = left_sum + right_sum + subroot.val
            all_sums.append(total_sum)
            return total_sum

        total = tree_sum(root)
        best = 0
        for s in all_sums:
            best = max(best, s * (total - s))
        return best % (10 ** 9 + 7)

# solution 2: 1 pass solution
# space: O(n)