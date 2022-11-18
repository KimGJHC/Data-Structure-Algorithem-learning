"""
1472. Design Browser History
You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) Visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.

# double linked list is a good option
# could use skip list to fasten back and forward
"""


class Node:
    def __init__(self, val=None):
        self.prev = None
        self.nxt = None
        self.val = val


class BrowserHistory:

    def __insert(self, node):
        # insert a node before self.tail
        prev = self.tail.prev
        prev.nxt = node
        self.tail.prev = node
        node.nxt = self.tail
        node.prev = prev

    def __deleteForward(self, node):
        # delete all node after current node
        node.nxt = self.tail
        self.tail.prev = node

    def __init__(self, homepage: str):
        self.head = Node()
        self.tail = Node()
        self.head.nxt = self.tail
        self.tail.prev = self.head

        node = Node(homepage)
        self.__insert(node)
        self.current = node

    def visit(self, url: str) -> None:
        self.__deleteForward(self.current)
        node = Node(url)
        self.__insert(node)
        self.current = node

    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev != self.head:
            self.current = self.current.prev
            steps -= 1
        return self.current.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.nxt != self.tail:
            self.current = self.current.nxt
            steps -= 1
        return self.current.val