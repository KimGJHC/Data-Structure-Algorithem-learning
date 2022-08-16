import heapq

if __name__ == '__main__':
    a = [5, 3, 4, 1, 2]
    heapq.heapify(a)
    for _ in range(5):
        print(a[0])
        print(heapq.heappop(a))
        print('-'*10)

