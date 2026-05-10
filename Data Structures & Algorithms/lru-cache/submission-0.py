class Node:
    def __init__(self, key: int, value: int):
        self.key, self.val = key, value
        self.prev = self.next = None

class LRUCache:
    """
    1) need a quick lookup O(1) - maybe dict with key being the int and value being a Node pointer 
    2) need setter that will:
        a) call getter and update if found
        c) create if not already exists
        b) mark key as recently used
    """
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.least_recent, self.most_recent = Node(0,0), Node(0,0)
        self.least_recent.next, self.most_recent.prev = self.most_recent, self.least_recent

    def remove(self, root: Node) -> None:
        root.prev.next, root.next.prev = root.next, root.prev
        return

    def insert(self, root: Node) -> None:
        temp = self.most_recent.prev
        temp.next, root.prev = root, temp
        root.next, self.most_recent.prev = self.most_recent, root
        return

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.remove(self.cache[key])
        self.insert(self.cache[key]) # move to most recent
        return self.cache[key].val
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        # if the new pair causes us to exceed cap, remove lru
        if len(self.cache) > self.cap:
            lru = self.least_recent.next
            self.remove(lru)
            del self.cache[lru.key]


        
