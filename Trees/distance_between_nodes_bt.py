#1740

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:

        if p == q:
            return 0
        
        graph = collections.defaultdict(list)

        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)

                queue.append(node.left)

            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
            
                queue.append(node.right)
            
        queue = collections.deque([(p, 0)])
        visited = set([p])

        while queue:
            cur_node, steps = queue.popleft()

            if cur_node == q:
                return steps
            else:
                for edge in graph[cur_node]:
                    if edge not in visited:
                        visited.add(edge)
                        queue.append((edge, steps + 1))
        

# Using LCA
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        def lowestAncestor(root, p, q):
            if root is None:
                return None
            
            if root.val == p or root.val == q:
                return root
            
            left = lowestAncestor(root.left, p, q)
            right = lowestAncestor(root.right, p, q)
            
            if left and right:
                return root
            
            return left if right is None else right
        lca = lowestAncestor(root, p, q)
        
        def dist(root, p):
            if root:
                if root.val == p:
                    return 0
                left = dist(root.left, p)
                right = dist(root.right, p)
                return 1+ min(left,right)
            return float('inf')
        
        return dist(lca, p) + dist(lca, q)