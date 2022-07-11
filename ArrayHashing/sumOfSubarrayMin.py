"""
907. Sum of Subarray Minimums

Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

Input: arr = [3,1,2,4]
Output: 17

Input: arr = [11,81,94,43,3]
Output: 444
"""

def sumSubarrayMins_v1(arr):
    n = len(arr)
    subarray_min = [float('inf')] * n
    res = 0

    for i, num in enumerate(arr):
        for j in range(i+1):
            subarray_min[j] = min(subarray_min[j], num)
            res += subarray_min[j]
    return res % (10**9+7)
# time: O(n!)
# space: O(n)
# This is too slow,

def sumSubarrayMins(arr):
    arr = [0] + arr
    res = [0] * len(arr)
    stack = [0]
    for i in range(len(arr)):
        while arr[stack[-1]] > arr[i]:
            stack.pop()
        j = stack[-1]
        res[i] = res[j] + (i-j) * arr[i]
        stack.append(i)
    return sum(res) % (10**9 + 7)

# time: O(n)
# space: O(n)

def test():
    arr = [3,1,2,4]
    # assert sumSubarrayMins(arr) == 17
    arr = [11,81,94,43,3]
    assert sumSubarrayMins(arr) == 444
    print("All tests passed!")