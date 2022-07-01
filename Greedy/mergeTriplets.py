"""
1899. Merge Triplets to Form Target Triplet

A triplet is an array of three integers. You are given a 2D integer array triplets, where triplets[i] = [ai, bi, ci] describes the ith triplet. You are also given an integer array target = [x, y, z] that describes the triplet you want to obtain.

To obtain target, you may apply the following operation on triplets any number of times (possibly zero):

Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5], triplets[j] will be updated to [max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5].
Return true if it is possible to obtain the target triplet [x, y, z] as an element of triplets, or false otherwise.

Input: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
Output: true

Input: triplets = [[3,4,5],[4,5,6]], target = [3,2,5]
Output: false

Input: triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]
Output: true
"""


def mergeTriplet(triplets, target):
    Satisfied = set()

    for triplet in triplets:
        for idx in [i for i in (0, 1, 2) if i not in Satisfied]:
            if triplet[idx] == target[idx]:
                other_idx1, other_idx2 = (idx+1)%3, (idx+2)%3
                if triplet[other_idx1] <= target[other_idx1] and triplet[other_idx2] <= target[other_idx2]:
                    Satisfied.add(idx)
        if len(Satisfied) == 3:
            break
    return len(Satisfied) == 3

# time: O(n)
# space: O(1)

def test():
    triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
    target = [2, 7, 5]
    assert mergeTriplet(triplets, target) == True
    triplets = [[3,4,5],[4,5,6]]
    target = [3,2,5]
    assert mergeTriplet(triplets, target) == False
    triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]
    target = [5,5,5]
    assert mergeTriplet(triplets, target) == True
    print("All tests passed!")

