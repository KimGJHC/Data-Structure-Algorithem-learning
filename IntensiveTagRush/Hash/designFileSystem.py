"""
1166. Design File System
You are asked to design a file system that allows you to create new paths and associate them with different values.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string "" and "/" are not.

Implement the FileSystem class:

bool createPath(string path, int value) Creates a new path and associates a value to it if possible and returns true. Returns false if the path already exists or its parent path doesn't exist.
int get(string path) Returns the value associated with path or returns -1 if the path doesn't exist.
"""


class FileSystem:

    def __init__(self, val=None):
        self.children = {}  # {pathname: FileSystem}
        self.val = val

    def createPath(self, path: str, value: int) -> bool:
        path = path.split('/')
        path = path[1:]

        n = len(path)
        current = self
        for i, sub in enumerate(path):
            if i == n - 1:
                if sub in current.children:
                    return False
                else:
                    current.children[sub] = FileSystem(value)
                    return True
            else:
                if sub in current.children:
                    current = current.children[sub]
                else:
                    return False

    def get(self, path: str) -> int:
        path = path.split('/')
        path = path[1:]

        current = self
        for sub in path:
            if sub in current.children:
                current = current.children[sub]
            else:
                return -1
        return current.val
