"""
once an unseen key-val pair comes and cache is full, delete the key-pair with smallest freq, add the new pair into cache and reset min freq to be 1
"""

from collections import defaultdict, OrderedDict


class Node:
    def __init__(self, key, val, freq):
        self.key = key
        self.val = val
        self.freq = freq


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minFreq = 0
        self.key2Node = {}
        self.freq2Node = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.key2Node:
            return -1
        else:
            node = self.key2Node[key]
            self.freq2Node[node.freq].pop(node.key)

            if not self.freq2Node[node.freq]:
                self.freq2Node.pop(node.freq)

            node.freq += 1
            self.freq2Node[node.freq][key] = node

            if self.minFreq not in self.freq2Node:
                self.minFreq += 1

            return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key2Node:
            self.key2Node[key].val = value
            self.get(key)
            return
        else:
            if len(self.key2Node) == self.capacity:
                k, n = self.freq2Node[self.minFreq].popitem(last=False)
                self.key2Node.pop(k)

            self.freq2Node[1][key] = self.key2Node[key] = Node(key, value, 1)
            self.minFreq = 1
            return
