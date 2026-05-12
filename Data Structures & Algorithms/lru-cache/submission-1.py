class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = collections.defaultdict(int)
        self.least_recent = Node(0,0)
        self.recent = Node(0,0)
        self.least_recent.next, self.recent.prev = self.recent, self.least_recent

    def insert(self, node: Node) -> None:
        prev, next_node = self.recent.prev, self.recent
        prev.next = next_node.prev = node
        node.next, node.prev = next_node, prev

    def remove(self, node: Node) -> None:
        prev, next_node = node.prev, node.next
        prev.next, next_node.prev = next_node, prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.least_recent.next
            self.remove(lru)
            del self.cache[lru.key]

