import random
class Node:
    def __init__(self, key, level):
        self.key = key
        self.forward = [None] * (level + 1) # references from key to node in different level

class SkipList:

    def __init__(self, max_level, P):
        self.MAXLEVEL = max_level
        self.P = P # percentages of nodes in level i
        self.head = self.__createNode(-1, self.MAXLEVEL)
        self.level = 0

    def __str__(self):
        res = "\n*****Skip List******\n"
        head = self.head
        for level in range(self.level + 1):
            res += "Level {}: ".format(level)
            node = head.forward[level]
            while (node != None):
                res += "{} ".format(node.key)
                node = node.forward[level]
            res += "\n"

        return res

    def __createNode(self, key, level):
        node = Node(key, level)
        return node

    def __getRandomLevel(self):
        level = 0
        while random.random() < self.P and level < self.MAXLEVEL:
            level += 1
        return level

    def insertKey(self, key):
        update = [None] * (self.MAXLEVEL + 1)
        current = self.head

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current == None or current.key != key:
            update_level = self.__getRandomLevel()
            if update_level > self.level:
                for i in range(self.level+1, update_level+1):
                    update[i] = self.head
                self.level = update_level

            node = self.__createNode(key, update_level)

            for i in range(update_level+1):
                node.forward[i] = update[i].forward[i]
                update[i].forward[i] = node
    def deleteKey(self, key):
        update = [None] * (self.MAXLEVEL+1)
        current = self.head

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current != None and current.key == key:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

        while self.level > 0and self.head.forward[self.level] == None:
            self.level -= 1

    def searchKey(self, key):
        current = self.head

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
        current = current.forward[0]

        if current and current.key == key:
            return True
        else:
            return False

def test():
    arr = [3, 5, 2, 6, 9]
    skiplist = SkipList(5, 0.5)
    for num in arr:
        skiplist.insertKey(num)
        print(skiplist)
        