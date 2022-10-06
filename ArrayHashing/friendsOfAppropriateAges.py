"""
825. Friends Of Appropriate Ages
There are n persons on a social media website. You are given an integer array ages where ages[i] is the age of the ith person.

A Person x will not send a friend request to a person y (x != y) if any of the following conditions is true:

age[y] <= 0.5 * age[x] + 7
age[y] > age[x]
age[y] > 100 && age[x] < 100
Otherwise, x will send a friend request to y.

Note that if x sends a request to y, y will not necessarily send a request to x. Also, a person will not send a friend request to themself.

Return the total number of friend requests made.
"""


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        c = Counter(ages)
        return sum(self.willSendReq(a, b) * c[a] * (c[b] - (a == b)) for a in c for b in c)

    def willSendReq(self, x, y):
        if y <= 0.5 * x + 7 or y > x or (y > 100 and x < 100):
            return False
        else:
            return True