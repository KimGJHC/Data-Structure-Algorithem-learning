def binarySearchxly(nums, target):
    l, r = 0, len(nums)

    while l < r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid
    return -1

def binarySearchxleqy(nums, target):
    l, r = 0, len(nums)-1

    while l <= r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid -1
    return -1

def binarySearchGetLargestIndex(nums, target):
    # return largest index that is smaller than or equal to target
    l, r = 0, len(nums)-1
    while l <= r:
        mid = (l+r)//2
        if nums[mid] <= target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
    return l - 1

def binarySearchGetSmallestIndex(nums, target):
    # return smallest index that is larger than or equal to target
    l, r = 0, len(nums)-1
    while l < r:
        mid = (l+r)//2
        if nums[mid] >= target:
            r = mid
        elif nums[mid] < target:
            l = mid + 1
    return r

def searchInsertPosition(nums, target):
    l, r = 0, len(nums)
    while l < r:
        mid = (l+r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l

def searchInsertPosition2(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        mid = (l+r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return r+1
