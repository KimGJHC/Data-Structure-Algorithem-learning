"""
670. Maximum Swap
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.
"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = [int(n) for n in list(str(num))]

        i = 0
        while i < len(nums) - 1:
            if nums[i] >= nums[i + 1]:
                i += 1
            else:
                break

        if i == len(nums) - 1:
            return num

        maxx = max(nums[i:])

        maxx_idx = None

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == maxx:
                maxx_idx = i
                break

        for i in range(maxx_idx):
            if nums[i] < maxx:
                nums[i], nums[maxx_idx] = nums[maxx_idx], nums[i]
                break

        res = [str(n) for n in nums]
        res = ''.join(res)
        res = int(res)

        return res
# time: O(n) where n = len(str(num))
# space: O(n)