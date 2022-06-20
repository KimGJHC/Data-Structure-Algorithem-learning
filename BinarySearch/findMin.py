    if len(nums) == 1:
        return nums[0]

    l, r = 0, len(nums)-1
    while l <= r:
        mid = (l+r)//2
        # notet that id mid = 0, it will compare to nums[-1]
        if nums[mid] < nums[mid-1]:
            return nums[mid]
        if nums[mid] >= nums[0]:
            if nums[-1] < nums[0]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            r = mid - 1



