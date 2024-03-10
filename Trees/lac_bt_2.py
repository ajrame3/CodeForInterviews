#1644

class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        def dfs(root, p, q):

            if root == p:
                return root
            if root == q:
                return q

            left, right = None, None

            if root.left:
                left = dfs(root.left, p, q)
            if root.right:
                right = dfs(root.right, p, q)

            if left and right:
                return root
            else:
                return left or right
                
        result = dfs(root, p, q)

        if result == None or result != p and result != q:
            return result
        else:
            if (result == p and dfs(result, q, q) == None) or (
                result == q and dfs(result, p, p) == None
            ):
                return None
            else:
                return result