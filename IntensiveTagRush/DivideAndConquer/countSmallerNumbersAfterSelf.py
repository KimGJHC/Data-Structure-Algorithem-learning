"""
315. Count of Smaller Numbers After Self

Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].
"""


class Solution:
    def countSmaller(self, nums):
        n = len(nums)
        arr = [[v, i] for i, v in enumerate(nums)]
        res = [0] * n

        def merge_sort(arr, left, right):
            if right - left <= 1:
                return
            mid = (right + left) // 2
            merge_sort(arr, left, mid)
            merge_sort(arr, mid, right)
            merge(arr, left, right, mid)

        def merge(arr, left, right, mid):
            i = left
            j = mid
            temp = []
            while i < mid and j < right:
                if arr[i][0] <= arr[j][0]:
                    res[arr[i][1]] += j - mid
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1

            while i < mid:
                res[arr[i][1]] += j - mid
                temp.append(arr[i])
                i += 1
            while j < right:
                temp.append(arr[j])
                j += 1
            for i in range(left, right):
                arr[i] = temp[i - left]

        merge_sort(arr, 0, n)

        return res