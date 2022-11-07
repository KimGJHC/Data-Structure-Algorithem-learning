"""
Segment tree is a data structure that stores information about array intervals as a tree
This helps range queries over an array, i.e. find sum(arr[l:r])
Segment tree needs linear amount of memory
Segment tree should handle 1. sum query 2. change values in O(logn) time

"""


class SegmentTree:

    def __init__(self, arr):
        self.tree = [None] * (4 * len(arr))
        self.__build(arr, 1, 0, len(arr)-1)

    def __build(self, arr, v, l, r):
        """
        Build the segment tree
        :param arr: input array
        :param v: index of current vertex in tree (array representation of tree)
        :param l: left boundary inclusive on arr
        :param r: right boundary inclusive on arr
        :return: None
        """
        if l == r:
            self.tree[v] = arr[l]
        else:
            mid = (l+r)//2
            self.__build(arr, v*2, l, mid)
            self.__build(arr, v*2+1, mid+1, r)
            self.tree[v] = self.tree[v*2] + self.tree[v*2+1]

    def sum(self, v, l, r, l_bound, r_bound):
        if l_bound > r_bound:
            return 0
        if (l == l_bound) and (r == r_bound):
            return self.tree[v]
        mid = (l+r)//2
        res = self.sum(v*2, l, mid, l_bound, min(r_bound, mid)) + \
              self.sum(v*2 + 1, mid+1, r, max(l_bound, mid+1), r_bound)
        return res

    def update(self, v, l, r, position, new_value):
        """
        :param v:
        :param l:
        :param r:
        :param position: position in tree
        :param new_value:
        :return:
        """
        if l == r:
            self.tree[v] = new_value
        else:
            mid = (l+r)//2
            if position <= mid:
                self.update(v*2, l, mid, position, new_value)
            else:
                self.update(v*2+1, mid+1, r, position, new_value)
            self.tree[v] = self.tree[v*2] + self.tree[v*2+1]


def testSegmentTree():
    arr = [1, 3, -2, 8, -7]
    n = len(arr)
    tree = SegmentTree(arr)
    print(tree.tree)
    assert tree.tree == [None, 3, 2, 1, 4, -2, 8, -7, 1, 3, None, None, None, None, None, None, None, None, None, None]
    print("result: {}; Expect: {}".format(tree.sum(1, 0, n-1, 2, 4), -1))
    assert tree.sum(1, 0, n-1, 2, 4) == -1
    tree.update(1, 0, n-1, 3, 5)
    arr2 = [1, 3, -2, 5, -7]
    tree2 = SegmentTree(arr2)
    print("result: {}; Expect: {}".format(tree.tree, tree2.tree))
    assert tree.tree == tree2.tree
    print("All tests passed")
