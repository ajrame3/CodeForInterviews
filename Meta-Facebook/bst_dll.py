class Node:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Convert:
    def tree_to_dll(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return None

        self.head = None
        self.tail = None

        self.inorder(root)

        self.head.left = self.tail
        self.tail.right = self.head

        return self.head
    
    def inorder(self, node: Node):
        if node:
            self.inorder(node.left)

            if not self.tail:
                self.head = node
            else:
                node.left = self.tail
                self.tail.right = node
            
            self.tail = Node
            self.inorder(node.right)