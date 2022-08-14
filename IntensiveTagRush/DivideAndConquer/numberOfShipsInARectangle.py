"""
1274. Number of Ships in a Rectangle

(This problem is an interactive problem.)

Each ship is located at an integer point on the sea represented by a cartesian plane, and each integer point may contain at most 1 ship.

You have a function Sea.hasShips(topRight, bottomLeft) which takes two points as arguments and returns true If there is at least one ship in the rectangle represented by the two points, including on the boundary.

Given two points: the top right and bottom left corners of a rectangle, return the number of ships present in that rectangle. It is guaranteed that there are at most 10 ships in that rectangle.

Submissions making more than 400 calls to hasShips will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.
"""


class Sea:
   def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:

class Point:
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y

class Solution:
    def countShips(self, sea, topRight, bottomLeft):
        if (bottomLeft.x > topRight.x) or (bottomLeft.y > topRight.y):
            return 0
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        if (topRight.x == bottomLeft.x) and (topRight.y == bottomLeft.y):
            return 1

        mid_x = (topRight.x + bottomLeft.x) // 2
        mid_y = (topRight.y + bottomLeft.y) // 2

        return self.countShips(sea, Point(mid_x, mid_y), bottomLeft) + \
               self.countShips(sea, topRight, Point(mid_x + 1, mid_y + 1)) + \
               self.countShips(sea, Point(mid_x, topRight.y), Point(bottomLeft.x, mid_y + 1)) + \
               self.countShips(sea, Point(topRight.x, mid_y), Point(mid_x + 1, bottomLeft.y))

