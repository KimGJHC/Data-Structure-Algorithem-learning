"""
1610. Maximum Number of Visible Points
You are given an array points, an integer angle, and your location, where location = [posx, posy] and points[i] = [xi, yi] both denote integral coordinates on the X-Y plane.

Initially, you are facing directly east from your position. You cannot move from your position, but you can rotate. In other words, posx and posy cannot be changed. Your field of view in degrees is represented by angle, determining how wide you can see from any given view direction. Let d be the amount in degrees that you rotate counterclockwise. Then, your field of view is the inclusive range of angles [d - angle/2, d + angle/2].

You can see some set of points if, for each point, the angle formed by the point, your position, and the immediate east direction from your position is in your field of view.

There can be multiple points at one coordinate. There may be points at your location, and you can always see these points regardless of your rotation. Points do not obstruct your vision to other points.

Return the maximum number of points you can see.
"""

import math, collections
class Solution:
    def visiblePoints(self, points, angle, location):
        n = len(points)
        if angle >= 360:
            return n

        points_at_location = 0
        degrees = []
        for point in points:
            if point[0] == location[0] and point[1] == location[1]:
                points_at_location += 1
            else:
                degrees.append(self.getDegree(location, point))
        if points_at_location == n:
            return n

        degrees.sort()
        max_degree = degrees[-1]
        over_degree = max_degree + angle - 360
        for i in range(len(degrees)):
            if degrees[i] <= over_degree:
                degrees.append(degrees[i] + 360)

        max_view_points = 0
        queue = collections.deque([])
        max_view_degree = angle
        min_view_degree = 0
        for degree in degrees:
            if min_view_degree <= degree <= max_view_degree:
                queue.append(degree)
            elif degree > max_view_degree:
                max_view_degree = degree
                min_view_degree = max_view_degree - angle
                queue.append(degree)
                while queue[0] < min_view_degree:
                    queue.popleft()
            max_view_points = max(max_view_points, len(queue))
        return max_view_points + points_at_location

    def getDegree(self, location, point):
        # return the degree between location-point line and E direction
        x_location, y_location = location
        x_point, y_point = point
        x_diff, y_diff = x_point - x_location, y_point - y_location

        if x_diff == 0:
            if y_diff > 0:
                return 90
            else:
                return 270
        elif y_diff == 0:
            if x_diff > 0:
                return 0
            else:
                return 180
        else:
            if x_diff > 0 and y_diff > 0:
                return math.degrees(math.atan(y_diff / x_diff))
            elif x_diff < 0 and y_diff > 0:
                return 180 + math.degrees(math.atan(y_diff / x_diff))
            elif x_diff < 0 and y_diff < 0:
                return 180 + math.degrees(math.atan(y_diff / x_diff))
            else:
                return 360 + math.degrees(math.atan(y_diff / x_diff))
# solution 1: convert to degree and sort
# time: O(n) where n = len(points)
# space: O(n) in the worst case
