class Solution:
    def inorderTraversal(self, root):
        result = []

        def inorder(node):
            if node:
                inorder(node.left)         # Left
                result.append(node.val)    # Root
                inorder(node.right)        # Right

        inorder(root)
        return result
