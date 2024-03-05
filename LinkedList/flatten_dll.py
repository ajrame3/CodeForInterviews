# 430
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        curr = head
        stack = []
        dummy = Node(-1, None, None, None)
        new_curr = dummy

        while curr or stack:
            node = Node(curr.val, None, None, None)
            new_curr.next = node
            node.prev = new_curr
            new_curr = new_curr.next

            if curr.child:
                stack.append(curr)
                curr = curr.child
            else:
                curr = curr.next
            
            while not curr and stack:
                curr = stack.pop()
                curr = curr.next
        
        dummy.next.prev = None
        return dummy.next





        