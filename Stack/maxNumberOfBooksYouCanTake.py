"""
2355. Maximum Number of Books You Can Take

You are given a 0-indexed integer array books of length n where books[i] denotes the number of books on the ith shelf of a bookshelf.

You are going to take books from a contiguous section of the bookshelf spanning from l to r where 0 <= l <= r < n. For each index i in the range l <= i < r, you must take strictly fewer books from shelf i than shelf i + 1.

Return the maximum number of books you can take from the bookshelf.
"""


class Solution:
    def maximumBooks(self, books):
        if not books:
            return 0

        stack = [books[0]]
        max_book = 0

        for i in range(1, len(books)):
            book = books[i]
            if book > stack[-1]:
                stack.append(book)
            else:  # book < top stack
                # update max number
                max_book = max(max_book, sum(stack))
                # update stack
                pre_max = book - 1  # the largest number of books we can take from stack top

                new_dist = [book]
                while stack and pre_max > 0:
                    pre_book = stack.pop()
                    if pre_book >= pre_max:
                        new_dist.append(pre_max)
                        pre_max -= 1
                    else:
                        new_dist.append(pre_book)
                        pre_max = pre_book - 1

                if pre_max <= 0:
                    stack = []
                while new_dist:
                    stack.append(new_dist.pop())

        max_book = max(max_book, sum(stack))
        return max_book
# solution 1: stack
# time: O(n**2)
# space: O(n)

    def maximumBooks_v2(self, books):
        n = len(books)
        dp, stack = [
                        0] * n, []  # dp[i] is max number of books we can take from shelves 0 to i and we must take all books from i
        for i in range(n):
            if books[i] == 0:
                stack.append(i)
                continue
            while stack:
                j = stack[-1]
                if books[j] >= books[i] - (i - j):
                    stack.pop()
                else:
                    break
            if not stack:
                j = -1
            if books[i] - i + j + 1 < 0:
                dp[i] = books[i] * (books[i] + 1) // 2
            else:
                dp[i] = (books[i] + books[i] - i + j + 1) * (i - j) // 2
            if j >= 0:
                dp[i] += dp[j]
            stack.append(i)

        return max(dp)

# solution 2: stack + dp
# time: O(n)
# space: O(n)
