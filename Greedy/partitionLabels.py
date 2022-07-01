"""
763. Partition Labels

You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]

Input: s = "eccbbbbdec"
Output: [10]
"""

# The key in this question is that when we encounter a visited letter, we need to know what is its group and join every thing afterwards
# Note that the group that the letter first appear will be the final group

def partitionLabels_v1(s):
    group = {}
    res = []

    for letter in s:
        # if we have not visited the letter
        res.append(letter)
        if letter not in group:
            group[letter] = len(res) - 1
        # if we have visited the letter
        else:
            letter_group = group[letter]
            res = res[:letter_group] + [''.join(res[letter_group:])]
            # update group
            for l in set(res[-1]):
                group[l] = len(res) - 1
    return [len(label) for label in res]

# time: O(n^2)
# space: O(n)

# because we need to update group each time we merge, it is not efficient
# a group is defined by its left and right boundary
def partitionLabels(s):
    last = {c: i for i, c in enumerate(s)}
    j = anchor = 0
    res = []
    for i, c in enumerate(s):
        j = max(j, last[c])
        if i == j:
            res.append(i - anchor + 1)
            anchor = i + 1
    return res

# time: O(n)
# space: O(1)

def test():
    s = "ababcbacadefegdehijhklij"
    s = "ababcbacadefegdehijhklij"
    assert partitionLabels(s) == [9,7,8]
    s = "eccbbbbdec"
    assert partitionLabels(s) == [10]
    print("All tests passed!")