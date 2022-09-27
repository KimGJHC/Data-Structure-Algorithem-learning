class Node:

    def __init__(self):
        self.key = None
        self.val = None
        self.prev = None
        self.nxt = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.memo = {}  # key = key, value = Node
        self.head, self.tail = Node(), Node()

        self.head.nxt = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.memo:
            node = self.memo[key]
            self.__move_to_head(node)  # move node after self.head
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.memo:
            node = self.memo[key]
            node.val = value
            self.__move_to_head(node)
        else:
            node = Node()
            node.key = key
            node.val = value

            self.__insert(node)
            self.memo[key] = node
            self.size += 1

            if self.size > self.capacity:
                deleted_node = self.__pop()
                self.memo.pop(deleted_node.key)
                self.size -= 1

    def __move_to_head(self, node):
        # move node to self.head.nxt
        self.__delete(node)
        self.__insert(node)

    def __insert(self, node):
        # insert node after self.head
        node.prev = self.head
        node.nxt = self.head.nxt

        node.nxt.prev = node
        self.head.nxt = node

    def __pop(self):
        # pop the last element of the DLL
        tail = self.tail.prev
        self.__delete(tail)
        return tail

    def __delete(self, node):
        # remove the node from DDL
        prev = node.prev
        nxt = node.nxt

        prev.nxt = nxt
        nxt.prev = prev
# DLL + hashmap
# time: O(1)