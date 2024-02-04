class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:

        self.res = None
        
        def helper(node):

            if not node or self.res: return

            helper(node.left)

            if node.val > p.val and not self.res:
                self.res = node
                return
            helper(node.right)
        
        helper(root)
        return self.res