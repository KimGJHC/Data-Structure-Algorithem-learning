"""
1851. Minimum Interval to Include Each Query

You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.

You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

Return an array containing the answers to the queries.

Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]

Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
Output: [2,-1,4,6]
"""
import heapq

def minInterval(intervals, queries):
    intervals.sort()
    minHeap = []
    i = 0
    ht = {}
    n = len(intervals)

    for query in sorted(queries):
        while i < n and intervals[i][0] <= query:
            s, e = intervals[i]
            heapq.heappush(minHeap, (e - s + 1, e))
            i += 1

        while minHeap and minHeap[0][1] < query:
            heapq.heappop(minHeap)
        ht[query] = minHeap[0][0] if minHeap else -1
    return [ht[query] for query in queries]

# time: O(nlogn)
# space: O(n + q)

def test():
    intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
    queries = [2, 3, 4, 5]
    assert minInterval(intervals, queries) == [3,3,1,4]
    intervals = [[2,3],[2,5],[1,8],[20,25]]
    queries = [2,19,5,22]
    assert minInterval(intervals, queries) == [2,-1,4,6]
    print("All tests passed!")