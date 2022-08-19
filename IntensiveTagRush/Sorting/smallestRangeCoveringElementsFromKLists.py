"""
632. Smallest Range Covering Elements from K Lists
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.
"""

import heapq
class Solution:
    def smallestRange(self, nums):
        heap = [(List[0], index, 0, len(List)) for index, List in enumerate(nums)]
        heapq.heapify(heap)

        max_val = max([List[0] for List in nums])
        res = [-1e9, 1e9]

        while heap:
            min_val, num_idx, list_idx, list_length = heapq.heappop(heap)

            if max_val - min_val < res[1] - res[0]:
                res = [min_val, max_val]

            if list_idx + 1 == list_length:
                return res

            next_num = nums[num_idx][list_idx + 1]
            max_val = max(max_val, next_num)
            heapq.heappush(heap, (next_num, num_idx, list_idx + 1, list_length))

# solution: heap tracking smallest values
# time: O(nlogk) where n = sum(lengths of array in nums) and k = len(nums)
# space: O(k)