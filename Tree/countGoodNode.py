"""
1448. Count Good Nodes in Binary Tree

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

"""
def goodNodes(root):
    res = 0

    def helper(node, prev_max):
        # this will add the number of good nodes in subtree root at node with previous maximum
        if not node:
            return
        nonlocal res
        if node.val >= prev_max:
            res += 1
            prev_max = node.val
        helper(node.left, prev_max)
        helper(node.right, prev_max)

    helper(root, float('-inf'))
    return res

