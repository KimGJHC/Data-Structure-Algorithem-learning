import collections
import heapq
def leastInterval(tasks, n):
    count = collections.Counter(tasks)
    heap = [ -v for v in count.values()]
    heapq.heapify(heap)
    time = 0
    queue = []

    while heap or queue:
        if queue:
            while queue and queue[0][1] == time:
                heapq.heappush(heap, queue.pop(0)[0])
        if heap:
            update = heapq.heappop(heap) + 1
            if update != 0:
                queue.append((update, time+n+1))
        time += 1
    return time