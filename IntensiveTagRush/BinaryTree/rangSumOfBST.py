"""
938. Range Sum of BST

Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].
"""


class Solution:
    def rangeSumBST(self, root, low, high):

        res = 0

        def inorder(root):
            nonlocal res
            if root:
                if root.val >= low:
                    inorder(root.left)
                    if root.val <= high:
                        inorder(root.right)
                        res += root.val
                    else:
                        return
                else:
                    if root.val <= high:
                        inorder(root.right)
                    return

        inorder(root)
        return res

# solution 1: inorder + truncate during traversal
# time: O(n)
# space: O(h)

# You better know how to do inorder traversal with iteration (stack)
    def rangeSumBST_v2(self, root, low, high):

        res = 0
        current = root
        stack = []

        while True:
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                if current.val >= low and current.val <= high:
                    res += current.val
                current = current.right
            else:
                break
        return res

# space: O(h)
