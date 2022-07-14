"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Input: height = [4,2,0,3,2,5]
Output: 9
"""

# This question is proved to be solvable with two pointers mimicing gradient descend
# In this solution we will use a monotonic decreasing stack

def trap(height):
    res = 0
    stack = []
    for i in range(len(height)):
        while stack and height[stack[-1]] < height[i]:
            smallest_height_idx = stack.pop()
            if not stack:
                break
            height_diff = min(height[i], height[stack[-1]]) - height[smallest_height_idx]
            length = i - 1 - stack[-1] if stack else -1
            res += height_diff * length
        stack.append(i)
    return res

# time: O(n)
# space: O(n)

def test():
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    assert trap(height) == 6
    height = [4,2,0,3,2,5]
    assert trap(height) == 9
    print("All tests passed!")