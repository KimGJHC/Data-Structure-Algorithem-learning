"""
846. Hand of Straights

Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true

Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
"""

from heapq import *
from collections import defaultdict
def isNStraightHand_V1(hand, groupSize):
    n = len(hand)
    if n % groupSize != 0:
        return False

    heapify(hand)
    need = defaultdict(int)

    while hand:
        current = heappop(hand)
        if need[current] > 0:
            need[current] -= 1
        else:
            for i in range(1, groupSize):
                need[current+i] += 1
    return sum(need.values()) == 0

# time: O(n)
# Space: O(n * groupSize)

# The logic is correct but the implementation might not be efficient
def isNStraightHand(hand, groupSize):
    n = len(hand)
    if n % groupSize != 0:
        return False
    if groupSize == 1:
        return True

    heapify(hand)
    have = defaultdict(int)
    for c in hand:
        have[c] += 1

    for i in range(n // groupSize):
        current = heappop(hand)
        while have[current] == 0:
            current = heappop(hand)

        for j in range(groupSize):
            have[current+j] -= 1
            if have[current+j] < 0:
                return False
    return True

# time: O(n)
# space: O(n)


def test():
    hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    groupSize = 3
    assert isNStraightHand(hand, groupSize) == True
    hand = [1,2,3,4,5]
    groupSize = 4
    assert isNStraightHand(hand, groupSize) == False
    print("All tests passed!")
