"""
767. Reorganize String

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

Input: s = "aab"
Output: "aba"

Input: s = "aaab"
Output: ""
"""
from collections import Counter
from heapq import *
def reorganizeString(s):
    # This is a two-pointers question, the left pointer will indicate the next unsatisfied position
    # right pointer is search for positions to compensate unsatisfied position
    # The two pointer is not working for 'abcdd'
    # lets think about create a new string from scratch
    ht = Counter(s)
    letter_count = [(-ht[key], key) for key in ht]
    heapify(letter_count)
    res = []

    while letter_count:
        most_count, most_key = heappop(letter_count)
        if not res:
            res.append(most_key)
            if most_count + 1 < 0:
                heappush(letter_count, (most_count + 1, most_key))
        else:
            if most_key == res[-1]:
                if not letter_count:
                    return ""
                else:
                    second_most_count, second_most_key = heappop(letter_count)
                    res.append(second_most_key)
                    if second_most_count + 1 < 0:
                        heappush(letter_count, (second_most_count + 1, second_most_key))
                    heappush(letter_count, (most_count, most_key))
            else:
                res.append(most_key)
                if most_count + 1 < 0:
                    heappush(letter_count, (most_count + 1, most_key))
    return ''.join(res)

# time: O(nlogn)
# space: O(n)

def test():
    s = "aab"
    assert reorganizeString(s) in ["aba"]
    s = "aaab"
    assert reorganizeString(s) == ""
    print("All tests passed!")

