#333

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        self.largest_value = 1

        self.dfs(root)

        return self.largest_value
    
    def dfs(self, node):
        if not node:
            return (False, 0, float("-inf"), float("inf"))
        
        if not node.left and not node.right:
            return (True, 1, node.val,  node.val)
        
        l_is_bst, l_size, l_min, l_max = self.dfs(node.left)
        r_is_bst, r_size, r_min, r_max = self.dfs(node.right)

        if l_is_bst and r_is_bst and l_max < node.val < r_min:
            cur_size = 1 + l_size + r_size
            self.largest_value = max(self.largest_value, cur_size)
            return (True, cur_size, l_min, r_max)
        
        elif l_is_bst and not node.right and l_max < node.val:
            cur_size = 1 + l_size
            self.largest_value = max(self.largest_value, cur_size)
            return (True, cur_size, l_min, node.val)
        
        elif r_is_bst and not node.left and node.val < r_min:
            cur_size = 1 + r_size
            self.largest_value = max(self.largest_value, cur_size)
            return (True, cur_size, node.val, r_max)
        
        else:
            return (False, 0, float("-inf"), float("inf"))

        