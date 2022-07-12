"""
1151. Minimum Swaps to Group All 1's Together

Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array together in any place in the array.

Input: data = [1,0,1,0,1]
Output: 1

Input: data = [0,0,0,1,0]
Output: 0

Input: data = [1,0,1,0,1,0,0,1,1,0,1]
Output: 3
"""

from collections import deque
def minSwaps_v1(data):
    # The key is to find a subarray with length of count_one that contains as more one as possible
    # A common practice for this is to maintain a queue/stack of indices and pop/append based on values
    count_one = sum(data)
    queue = deque([])
    max_count_one_subarray = 0

    for i, num in enumerate(data):
        if num == 1:
            queue.append(i)
            while i - queue[0] >= count_one:
                queue.popleft()
            max_count_one_subarray = max(max_count_one_subarray, len(queue))
    return count_one - max_count_one_subarray

# time: O(n)
# space: O(n)

def minSwaps(data):
    # sliding windows is also dorable
    window_size = sum(data)
    count_one = max_one = 0
    left = right = 0
    while right < len(data):
        count_one += data[right]
        right += 1
        if right - left > window_size:
            count_one -= data[left]
            left += 1
        max_one = max(max_one, count_one)
    return window_size - max_one

# time: O(n)
# space: O(1)


def test():
    data = [1, 0, 1, 0, 1]
    # assert minSwaps(data) == 1
    data = [0,0,0,1,0]
    # assert minSwaps(data) == 0
    data = [1,0,1,0,1,0,0,1,1,0,1]
    assert minSwaps(data) == 3
    print("All tests passed!")


