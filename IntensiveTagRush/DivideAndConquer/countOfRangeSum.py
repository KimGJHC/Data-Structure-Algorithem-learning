"""
327. Count of Range Sum

Given an integer array nums and two integers lower and upper, return the number of range sums that lie in [lower, upper] inclusive.

Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j inclusive, where i <= j.
"""


class Solution:
    def countRangeSum(self, nums, lower, upper):
        good_range_sum_count = 0

        def getRangeSumCount(nums, left, right):
            # return the rangeSum of nums[i:right] for right > i >= left and of nums[left:j]
            nonlocal good_range_sum_count
            if right - left == 1:
                if nums[left] >= lower and nums[left] <= upper:
                    good_range_sum_count += 1
                return [nums[left]], [nums[left]]  # range sum starting from left, from right
            else:
                mid = (right + left) // 2
                left_range_current, left_range = getRangeSumCount(nums, left, mid)
                right_range, right_range_current = getRangeSumCount(nums, mid, right)

                for left_sum in left_range:
                    for right_sum in right_range:
                        range_sum = left_sum + right_sum
                        if upper >= range_sum and range_sum >= lower:
                            good_range_sum_count += 1

            left_range_current = left_range_current[:]
            for right_val in range(mid, right):
                left_range_current.append(left_range_current[-1] + nums[right_val])

            right_range_current = right_range_current[:]
            for left_val in range(mid - 1, left - 1, -1):
                right_range_current.append(right_range_current[-1] + nums[left_val])

            return left_range_current, right_range_current

        getRangeSumCount(nums, 0, len(nums))
        return good_range_sum_count

# solution 1: Use divide and conquer, exceeds time limit
# time: O(n**2)

# other solutions:
# 1. prefix-sum + hashmap

# 2. prefix-sum + merge sort
        def getRangeSumCount_v2(nums, left, right):
            cumsum = [0]
            for n in nums:
                cumsum.append(cumsum[-1] + n)

            def mergeSort(l, r):
                if l == r:
                    return 0
                mid = (l+r) // 2
                cnt = mergeSort(l, mid) + mergeSort(mid+1, r)

                i = j = mid + 1

                for left in cumsum[l:mid+1]:
                    while i <= r and cumsum[i] - left < lower:
                        i += 1
                    while j <= r and cumsum[j] - left <= upper:
                        j += 1
                    cnt += j - i
                cumsum[l:r+1] = sorted(cumsum[l:r+1])
                return cnt
            return mergeSort(0, len(cumsum) - 1)

# time: O(nlogn)
# space: O(n)
