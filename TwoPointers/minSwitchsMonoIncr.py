"""
Min switch to make the string monotonically increasing
"""

def minSwitchMonoIncr(s):
    # The idea is to move l, r pointers from 0 and len(s)-1, switch if needed
    left, right = 0, len(s)-1
    res = 0
    while left < right:
        while s[left] == '0' and left < right:
            left += 1
        while s[right] == '1' and right > left:
            right -= 1
        if right > left:
            res += 1
            left += 1
            right -= 1
        else:
            break
    return res

def test():
    s = "00110"
    assert minSwitchMonoIncr(s) == 1
    s = "010110"
    assert minSwitchMonoIncr(s) == 1
    s = "00011000"
    assert minSwitchMonoIncr(s) == 2
    print("All tests passed!")
