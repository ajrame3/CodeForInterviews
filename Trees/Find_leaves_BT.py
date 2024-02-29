# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = collections.defaultdict(list)

        def dfs(node, layer):
            if not node:
                return layer
            
            left = dfs(node.left, layer)
            right = dfs(node.right, layer)

            layer = max(left, right)

            res[layer].append(node.val)

            return layer + 1
        
        dfs(root, 0)

        return res.values()
        


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        while root:
            temp = []
            root = self.solve(root, temp)
            result.append(temp)

        return result
    
    def solve(self, start: Optional[TreeNode], values: List[int]) -> Optional[TreeNode]:
        if start:
            left_child = start.left
            right_child = start.right

            if not left_child and not right_child:
                values.append(start.val)
                return None
            
            start.left = self.solve(start.left, values)
            start.right = self.solve(start.right, values)
        
        return start