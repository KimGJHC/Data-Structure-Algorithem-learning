"""
588. Design In-Memory File System

Design a data structure that simulates an in-memory file system.

Implement the FileSystem class:

FileSystem() Initializes the object of the system.
List<String> ls(String path)
If path is a file path, returns a list that only contains this file's name.
If path is a directory path, returns the list of file and directory names in this directory.
The answer should in lexicographic order.
void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well.
void addContentToFile(String filePath, String content)
If filePath does not exist, creates that file containing given content.
If filePath already exists, appends the given content to original content.
String readContentFromFile(String filePath) Returns the content in the file at filePath.

Input
["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
[[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
Output
[null, [], null, null, ["a"], "hello"]
"""


class FileSystem_v1:
    # we can use a dictionary to store
    # we need sorting algorithm for ls
    def __init__(self):
        self.directory = {'': ['d', {}]}

    def ls(self, path):
        paths = path.split('/')
        if paths[-1] == '':
            paths.pop()
        current_dir = self.directory
        for i in range(0, len(paths)-1):
            current_dir = current_dir[paths[i]][1]
        current_dir = current_dir[paths[-1]]
        if current_dir[0] == 'd':
            return sorted(current_dir[1].keys())
        elif current_dir[0] == 'f':
            return [paths[-1]]

    def mkdir(self, path):
        paths = path.split('/')
        if paths[-1] == '':
            paths.pop()
        current_dir = self.directory
        for i in range(0, len(paths)):
            if paths[i] not in current_dir:
                current_dir[paths[i]] = ['d', {}]
            current_dir = current_dir[paths[i]][1]

    def addContentToFile(self, filePath, content):
        filePaths = filePath.split('/')
        self.mkdir('/'.join(filePaths[:-1]))
        current_dir = self.directory
        for i in range(0, len(filePaths)-1):
            current_dir = current_dir[filePaths[i]][1]
        # add file
        file = filePaths[-1]
        if file in current_dir:
            current_dir[file][1] += content
        else:
            current_dir[file] = ['f', content]

    def readContentFromFile(self, filePath):
        filePaths = filePath.split('/')
        current_dir = self.directory
        for i in range(0, len(filePaths)-1):
            current_dir = current_dir[filePaths[i]][1]
        file = filePaths[-1]
        return current_dir[file][1]

# There are several ways to improve
# 1. We should not sort the key every time ls is called, we should maintain the order internally
# 2. We should use a tree structure to maintain order

from collections import defaultdict
class Node:
    def __init__(self):
        self.child = defaultdict(Node)
        self.content = ""


class FileSystem(object):

    def __init__(self):
        self.root = Node()

    def find(self, path):  # find and return node at path.
        curr = self.root
        if len(path) == 1:
            return self.root
        for word in path.split("/")[1:]:
            curr = curr.child[word]
        return curr

    def ls(self, path):
        curr = self.find(path)
        if curr.content:  # file path,return file name
            return [path.split('/')[-1]]
        return sorted(curr.child.keys())

    def mkdir(self, path):
        self.find(path)

    def addContentToFile(self, filePath, content):
        curr = self.find(filePath)
        curr.content += content

    def readContentFromFile(self, filePath):
        curr = self.find(filePath)
        return curr.content