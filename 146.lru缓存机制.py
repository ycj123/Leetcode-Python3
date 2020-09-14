#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#



# @lc code=start

class Node:
    def __init__(self, key, val):#double linked list node
        self.val = val
        self.key = key
        self.pre = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.cache = {}# hash map
        self.head.next = self.tail# double linked list
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:# miss
            return -1
        # not miss
        node = self.cache[key]
        self.remove(node)
        self.addtohead(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.cache:# already in LRU
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.addtohead(node)

        if len(self.cache)>self.cap:# overflow
            lastnode = self.tail.pre
            self.remove(lastnode)
            self.cache.pop(lastnode.key)

    def remove(self, node: "Node") -> None:
        pre = node.pre
        nxt = node.next
        pre.next = nxt
        nxt.pre = pre


    def addtohead(self, node: "Node") -> None:
        nxt = self.head.next
        self.head.next = node
        node.next = nxt
        node.pre = self.head
        nxt.pre = node
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

