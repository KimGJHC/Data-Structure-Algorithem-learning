class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        if not root:
            return res

        while True:
            while root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left
            root = stack.pop()

            if root.right and stack and root.right == stack[-1]:
                stack.pop()
                stack.append(root)
                root = root.right
            else:
                res.append(root.val)
                root = None

            if len(stack) <= 0:
                break
        return res
