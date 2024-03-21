from collections import defaultdict
import queue


class TreeNode:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right
    

class traversal:
    def vertical_order_traversal(self, root):
        if not root:
            return []
        
        col = defaultdict(list)
        q = queue([(root, 0)])

        while q:
            node, x = q.popleft()
            col[x].append(node.val)

            if node.left:
                q.append((node.left, x - 1))
            if node.right:
                q.append((node.right, x + 1))
        
        return [col[x] for x in range(min(col), max(col) + 1)]
    