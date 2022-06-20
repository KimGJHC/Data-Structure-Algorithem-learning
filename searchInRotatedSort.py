def search(nums, target):
    # nums is sorted and rotated by certain pivot
    l, r = 0, len(nums)-1

    while l <= r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[l]:
            if target >= nums[l] and target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if target < nums[l] and target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

    return -1
