"""
912. Sort an Array

Given an array of integers nums, sort the array in ascending order.
"""


class Solution:
    def sortArray(self, nums):

        def mergeSort(nums, left, right):
            # merge sort nums[left:right]
            if right - left <= 1:
                return

            mid = (right + left) // 2
            mergeSort(nums, left, mid)
            mergeSort(nums, mid, right)
            merge(nums, left, right, mid)

        def merge(nums, left, right, mid):
            i = left
            j = mid

            temp = []
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
        return nums

# solution 1: typical merge sort, recursive function looks like postorder traversal
# time: O(nlogn)
# space: O(n)
# good practice to other sorting algorithm