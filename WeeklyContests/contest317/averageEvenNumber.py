def averageValue(nums) -> int:
    total = 0
    count = 0

    for num in nums:
        if num % 3 == 0:
            total += num
            count += 1

    return total // count if count > 0 else 0

def test():
    nums = [1,3,6,10,12,15]
    assert averageValue(nums) == 9
    nums = [1,2,4,7,10]
    assert averageValue(nums) == 0
    print("done")