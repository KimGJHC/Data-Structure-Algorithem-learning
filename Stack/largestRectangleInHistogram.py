"""
84. Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Input: heights = [2,1,5,6,2,3]
Output: 10

Input: heights = [2,4]
Output: 4
"""

def largestRectangleArea(heights):
    # we will use a monotonic stack
    res = 0
    stack = []
    for i in range(len(heights)+1):
        while stack and (i == len(heights) or heights[stack[-1]] > heights[i]):
            height = heights[stack.pop()]
            if stack:
                # -1 because heights[i] will not be included in the rectangle we evaluate, we are evaluating height
                length = i - stack[-1] - 1
            else:
                length = i
            res = max(res, length * height)
        stack.append(i)
    return res

# Think about the rectangle with the smallest height at current bar
# time: O(n)
# space: O(n)

def test():
    heights = [2, 1, 5, 6, 2, 3]
    assert largestRectangleArea(heights) == 10
    heights = [2,4]
    assert largestRectangleArea(heights) == 4
    print("All tests passed!")
