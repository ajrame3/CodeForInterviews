# 432
class LinkedList:
    def __init__(self, val, cnt=0, next_node=None, prev_node=None):
        self.val = val
        self.cnt = cnt
        self.next_node = next_node
        self.prev_node = prev_node

class AllOne:

    def __init__(self):
        self.head = LinkedList(val='')
        self.tail = LinkedList(val='', cnt=float('inf'), prev_node=self.head)
        self.head.next_node = self.tail
        self.dict = {}
    
    def swap_nodes(self, node1, node2, node3, node4):
        node1.next_node = node3
        node3.prev_node, node3.next_node = node1, node2
        node2.prev_node, node2.next_node = node3, node4
        node4.prev_node = node2
        return (node1, node3, node2, node4)

    def inc(self, key: str) -> None:
        if key not in self.dict:
            p, c = self.head, self.head.next_node
            node = LinkedList(val=key, cnt=1, next_node=c, prev_node=p)
            p.next_node = node
            c.prev_node = node
            self.dict[key] = node
            return
        
        node = self.dict[key]
        node.cnt += 1

        while node.next_node.cnt < node.cnt:
            node1, node2, node, node4 = self.swap_nodes(node.prev_node, node, node.next_node, node.next_node.next_node)
            self.dict[key] = node
        
        
    def dec(self, key: str) -> None:
        node = self.dict[key]
        node.cnt -= 1
        if node.cnt == 0:
            p, n = node.prev_node, node.next_node
            p.next_node = n
            n.prev_node = p
            del self.dict[key]
            return
        while node.prev_node.cnt > node.cnt:
            node1, node, node3, node4 = self.swap_nodes(node.prev_node.prev_node, node.prev_node, node, node.next_node)
            self.dict[key] = node
    
    def getMaxKey(self) -> str:
        if self.tail.prev_node:
            return self.tail.prev_node.val
        return ''
    
    def getMinKey(self) -> str:
        if self.head.next_node:
            return self.head.next_node.val
        return ''
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()