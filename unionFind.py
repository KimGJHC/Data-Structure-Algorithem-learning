class DisjointSet(object):
    def __init__(self):
        self.parent = [-1] * 1001

    def find(self, x):
        if self.parent[x] >= 0:
            x = self.find(self.parent[x])
        return x

    def union(self, x, y):
        x_root, y_root = self.find(x), self.find(y)
        if x_root == y_root:  # x and y are already in the same set
            return False
        x_rank, y_rank = self.parent[x_root], self.parent[y_root]
        if x_rank < y_rank:
            self.parent[y_root] = x_root
        elif x_rank > y_rank:
            self.parent[x_root] = y_root
        else:
            self.parent[x_root] = y_root
            self.parent[y_root] -= 1
        return True

# The parent of root is rank which are negative
# edge can be regarded as union operation
# find is to find the root of the current node