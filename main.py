import heapq

if __name__ == '__main__':
    l = [['a', 3], ['b', 1]]

    def foo(x, y):
        return x[1] - y[1]

    heap = new_heapify(l, cmp=foo)
    new_heappop(heap)

