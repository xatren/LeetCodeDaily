class Node(object):
    def __init__(self, count=0):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne(object):
    def __init__(self):
        self.key_node = {}  # Maps keys to their corresponding nodes
        self.head = Node()  # Dummy head
        self.tail = Node()  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key):
        \\\
        :type key: str
        :rtype: None
        \\\
        if key not in self.key_node:
            # If the key doesn't exist, insert it with count 1
            if self.head.next.count != 1:
                self._add_node_after(Node(1), self.head)
            self.head.next.keys.add(key)
            self.key_node[key] = self.head.next
        else:
            # If the key exists, move it to the next count bucket
            curr_node = self.key_node[key]
            next_node = curr_node.next
            if next_node.count != curr_node.count + 1:
                self._add_node_after(Node(curr_node.count + 1), curr_node)
            next_node = curr_node.next
            next_node.keys.add(key)
            curr_node.keys.remove(key)
            self.key_node[key] = next_node
            if not curr_node.keys:
                self._remove_node(curr_node)

    def dec(self, key):
        \\\
        :type key: str
        :rtype: None
        \\\
        curr_node = self.key_node[key]
        if curr_node.count == 1:
            # If count becomes 0, remove the key
            del self.key_node[key]
        else:
            # Move the key to the previous count bucket
            prev_node = curr_node.prev
            if prev_node.count != curr_node.count - 1:
                self._add_node_after(Node(curr_node.count - 1), prev_node)
            prev_node = curr_node.prev
            prev_node.keys.add(key)
            self.key_node[key] = prev_node
        curr_node.keys.remove(key)
        if not curr_node.keys:
            self._remove_node(curr_node)

    def getMaxKey(self):
        \\\
        :rtype: str
        \\\
        if self.tail.prev == self.head:
            return \\
        return next(iter(self.tail.prev.keys))

    def getMinKey(self):
        \\\
        :rtype: str
        \\\
        if self.head.next == self.tail:
            return \\
        return next(iter(self.head.next.keys))

    def _add_node_after(self, node, prev_node):
        node.prev = prev_node
        node.next = prev_node.next
        node.prev.next = node
        node.next.prev = node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()