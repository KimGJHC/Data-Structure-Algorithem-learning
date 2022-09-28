class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            current = stack.pop()
            res.append(current.val)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return res