#450

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            # find in-order smallest succesor
            root.val = self.minValue(root.right).val

            root.right = self.deleteNode(root.right, root.val)
        
        return root

    def minValue(self, node):
        if node is None:
            return None
        
        while node.left:
            node = node.left
        
        return node