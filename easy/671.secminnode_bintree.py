class Solution:
    def findSecondMinimumValue(self, root):
        self.second_min = float('inf')
        self.root_val = root.val

        def dfs(node):
            if not node:
                return
            if self.root_val < node.val < self.second_min:
                self.second_min = node.val
            elif node.val == self.root_val:
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return self.second_min if self.second_min < float('inf') else -1
