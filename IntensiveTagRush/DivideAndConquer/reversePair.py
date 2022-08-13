"""
493. Reverse Pairs

Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] > 2 * nums[j].
"""


class Solution:
    def reversePairs(self, nums):
        pair_count = 0

        # use merge sort

        def mergeSort(nums, left, right):
            if right - left <= 1:
                return
            mid = (right + left) // 2
            mergeSort(nums, left, mid)
            mergeSort(nums, mid, right)
            merge(nums, left, right, mid)

        def merge(nums, left, right, mid):
            nonlocal pair_count

            # O(n)
            i, j = mid - 1, right - 1
            while i >= left and j >= mid:
                if nums[i] > 2 * nums[j]:
                    pair_count += j - mid + 1
                    i -= 1
                else:
                    j -= 1

            # O(n)
            temp = []
            i, j = left, mid
            while i < mid and j < right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1

            while i < mid:
                temp.append(nums[i])
                i += 1
            while j < right:
                temp.append(nums[j])
                j += 1

            for i in range(left, right):
                nums[i] = temp[i - left]

        mergeSort(nums, 0, len(nums))
        return pair_count

# solution: merge sort
# time: O(nlogn)
# space: O(n)