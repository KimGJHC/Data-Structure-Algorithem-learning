"""
1086. High Five
Given a list of the scores of different students, items, where items[i] = [IDi, scorei] represents one score from a student with IDi, calculate each student's top five average.

Return the answer as an array of pairs result, where result[j] = [IDj, topFiveAveragej] represents the student with IDj and their top five average. Sort result by IDj in increasing order.

A student's top five average is calculated by taking the sum of their top five scores and dividing it by 5 using integer division.

"""

# the idea is to use heap for top-k/bottom-k questions

from collections import defaultdict
import heapq

def highFive(items):
    top_scores = defaultdict(list)

    for Id, score in items:
        heapq.heappush(top_scores[Id], score)
        if len(top_scores[Id]) > 5:
            heapq.heappop(top_scores[Id])
    ids = list(top_scores.keys())
    return [[Id, sum(top_scores[Id]) // 5] for Id in sorted(ids)]

# time: O(nlogn)
# space: O(n)