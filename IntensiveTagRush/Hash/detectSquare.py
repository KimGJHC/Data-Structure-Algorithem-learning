"""
2013. Detect Squares

You are given a stream of points on the X-Y plane. Design an algorithm that:

Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.
An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

Implement the DetectSquares class:

DetectSquares() Initializes the object with an empty data structure.
void add(int[] point) Adds a new point point = [x, y] to the data structure.
int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.
"""


class DetectSquares:

    def __init__(self):
        self.count_points = collections.Counter()  # {(x,y): freq}
        self.x_coord = collections.defaultdict(set)

    def add(self, point: List[int]) -> None: #time O(1)
        x, y = point
        self.count_points[(x, y)] += 1
        self.x_coord[x].add(y)

    def count(self, point: List[int]) -> int: #time: O(n)
        x, y = point
        res = 0
        for y_cand in self.x_coord[x]:
            if y_cand != y:
                res += self.count_points[(x + y - y_cand, y)] * self.count_points[(x + y - y_cand, y_cand)] * \
                       self.count_points[(x, y_cand)]
                res += self.count_points[(x + y_cand - y, y)] * self.count_points[(x + y_cand - y, y_cand)] * \
                       self.count_points[(x, y_cand)]
        return res