from Interval.minIntervalInQuery import test


import heapq
if __name__ == '__main__':
    test = [5,2, 3, 4,1]
    heapq.heapify(test)

    while test:
         print(test[0])
         print(heapq.heappop(test))