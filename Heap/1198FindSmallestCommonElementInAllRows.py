"""
1198. Find Smallest Common Element in All Rows
Given an m x n matrix mat where every row is sorted in strictly increasing order, return the smallest common element in all rows.

If there is no common element, return -1.

# pop the first element of each row and maintain order of values to pop
"""


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        ROW, COL = len(mat), len(mat[0])

        queue_heads = []  # (value, row, col)
        for r in range(ROW):
            heapq.heappush(queue_heads, (mat[r][0], r, 0))

        while len(queue_heads) == ROW:
            max_head = queue_heads[-1][0]

            if queue_heads[0][0] == max_head:
                return max_head
            while queue_heads[0][0] < max_head:
                _, row_poped, col_poped = heapq.heappop(queue_heads)
                col_poped += 1
                if col_poped == COL:
                    return -1
                else:
                    heapq.heappush(queue_heads, (mat[row_poped][col_poped], row_poped, col_poped))
# time: O(nmlogm)
# space: O(m)