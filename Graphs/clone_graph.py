# 133 Clone Graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def helper(self, node, visited):
        if node is None:
            return None
            
        new_node = Node(node.val)
        visited[node.val] = new_node

        for adj_node in node.neighbors:
            if adj_node.val not in visited:
                new_node.neighbors.append(self.helper(adj_node, visited))  
            else:
                new_node.neighbors.append(visited[adj_node.val])

        return new_node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return self.helper(node, {})




