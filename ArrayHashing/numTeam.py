"""
1395. Count Number of Teams

There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).
"""


def numTeams(rating):
    res = 0
    n = len(rating)

    for i in range(1, n - 1):
        left_large = 0
        left_small = 0
        right_large = 0
        right_small = 0

        for j in range(i):
            if rating[j] < rating[i]:
                left_small += 1
            elif rating[j] > rating[i]:
                left_large += 1
        for k in range(i + 1, n):
            if rating[k] < rating[i]:
                right_small += 1
            elif rating[k] > rating[i]:
                right_large += 1
        res += left_small * right_large + left_large * right_small
    return res

# time: O(n**2)
# space: O(1)