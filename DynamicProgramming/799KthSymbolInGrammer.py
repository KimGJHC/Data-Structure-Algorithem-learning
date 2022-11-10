"""
779. K-th Symbol in Grammar
We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

# top down dp with states of n and k
"""


class Solution:

    @lru_cache(None)
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        last_layer_idx = (k + 1) // 2

        last_layer_value = self.kthGrammar(n - 1, last_layer_idx)

        if k % 2 == 1:
            if last_layer_value == 1:
                return 1
            else:
                return 0
        else:
            if last_layer_value == 0:
                return 1
            else:
                return 0

# time: O(n)
# space: O(logn)