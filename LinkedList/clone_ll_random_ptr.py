#138 Copy list with random pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None
        
        copy = {}

        copy[head] = Node(head.val)

        placeholder = head

        while head:
            if head.next and head.next not in copy:
                copy[head.next] = Node(head.next.val)
            copy[head].next = copy.get(head.next, None)

            if head.random and head.random not in copy:
                copy[head.random] = Node(head.random.val)
            copy[head].random = copy.get(head.random, None)

            head = head.next
        
        return copy[placeholder]
        