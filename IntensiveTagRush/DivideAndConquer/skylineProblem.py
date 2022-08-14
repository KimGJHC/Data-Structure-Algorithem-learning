"""
218. The Skyline Problem

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:

lefti is the x coordinate of the left edge of the ith building.
righti is the x coordinate of the right edge of the ith building.
heighti is the height of the ith building.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]
"""


class Solution:
    def getSkyline(self, buildings):
        n = len(buildings)
        if n == 0:
            return []
        if n == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
        mid = n // 2
        left_skyline = self.getSkyline(buildings[:mid])
        right_skyline = self.getSkyline(buildings[mid:])

        return self.mergeSkyline(left_skyline, right_skyline)

    def mergeSkyline(self, left_skyline, right_skyline):
        # merge 2 skylines
        merged_skyline = []
        height_current = 0
        left_current_height = 0
        right_current_height = 0

        left_n = len(left_skyline)
        right_n = len(right_skyline)

        i, j = 0, 0
        while i < left_n and j < right_n:
            left_x, left_height = left_skyline[i]
            right_x, right_height = right_skyline[j]
            if left_x < right_x:
                left_current_height = left_height
                x_current = left_x
                height_current = max(left_current_height, right_current_height)
                i += 1
            elif right_x < left_x:
                right_current_height = right_height
                x_current = right_x
                height_current = max(left_current_height, right_current_height)
                j += 1
            else:
                left_current_height = left_height
                right_current_height = right_height
                x_current = left_x
                height_current = max(left_current_height, right_current_height)
                i += 1
                j += 1
            if not merged_skyline or merged_skyline[-1][1] != height_current:
                merged_skyline.append([x_current, height_current])

        while i < left_n:
            merged_skyline.append(left_skyline[i])
            i += 1
        while j < right_n:
            merged_skyline.append(right_skyline[j])
            j += 1
        return merged_skyline

# time: O(nlogn)
# space: O(n)