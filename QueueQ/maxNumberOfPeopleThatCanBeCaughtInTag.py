"""
1989. Maximum Number of People That Can Be Caught in Tag
You are playing a game of tag with your friends. In tag, people are divided into two teams: people who are "it", and people who are not "it". The people who are "it" want to catch as many people as possible who are not "it".

You are given a 0-indexed integer array team containing only zeros (denoting people who are not "it") and ones (denoting people who are "it"), and an integer dist. A person who is "it" at index i can catch any one person whose index is in the range [i - dist, i + dist] (inclusive) and is not "it".

Return the maximum number of people that the people who are "it" can catch.
"""

from collections import deque
class Solution:
    def catchMaximumAmountofPeople(self, team: List[int], dist: int) -> int:
        zero_queue = deque()  # store index of 0
        one_queue = deque()
        res = 0

        for i, ppl in enumerate(team):
            if ppl == 0:
                if one_queue:
                    while one_queue:
                        if one_queue[0] >= i - dist:
                            break
                        one_queue.popleft()
                    if one_queue:
                        res += 1
                        one_queue.popleft()
                    else:
                        zero_queue.append(i)
                else:
                    zero_queue.append(i)
            else:
                if zero_queue:
                    while zero_queue:
                        if zero_queue[0] >= i - dist:
                            break
                        zero_queue.popleft()
                    if zero_queue:
                        res += 1
                        zero_queue.popleft()
                    else:
                        one_queue.append(i)
                else:
                    one_queue.append(i)
        return res
# time: O(n)
# space: O(n)