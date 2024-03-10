#426
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return None
        
        self.head = None
        self.tail = None

        self.inorder(root)

        self.head.left = self.tail
        self.tail.right = self.head

        return self.head

    def inorder(self, node):
        if node:
            self.inorder(node.left)

            if not self.tail:
                self.head = node
            else:
                node.left = self.tail
                self.tail.right = node
            
            self.tail = node

            self.inorder(node.right)