"""
494. Target Sum

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Input: nums = [1,1,1,1,1], target = 3
Output: 5

Input: nums = [1], target = 1
Output: 1
"""

def findTargetSum(nums, target):
    ht = {} # {(i, target): number of ways getting target with nums[:i]}
    total = sum(nums)

    def find(i, target):
        if i == 1:
            if target == nums[0] or target == -nums[0]:
                ht[(i, target)] = 1
                if target == 0:
                    ht[(i, target)] += 1
                return ht[(i, target)]
            else:
                ht[(i, target)] = 0
                return 0
        if target > total or target < -total:
            return 0
        if (i, target) in ht:
            return ht[(i, target)]
        else:
            total_ways = find(i-1, target+nums[i-1]) + find(i-1, target-nums[i-1])
            ht[(i, target)] = total_ways
            return total_ways
    return find(len(nums), target)

# time: O(target*n)
# space: O(target*n)

def test():
    nums = [1, 1, 1, 1, 1]
    target = 3
    assert findTargetSum(nums, target) == 5
    nums = [1]
    target = 1
    assert findTargetSum(nums, target) == 1
    nums = [0, 0, 1]
    target = 1
    assert findTargetSum(nums, target) == 4
    print("All tests passed!")