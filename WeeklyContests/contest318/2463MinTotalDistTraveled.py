"""
2463. Minimum Total Distance Traveled
There are some robots and factories on the X-axis. You are given an integer array robot where robot[i] is the position of the ith robot. You are also given a 2D integer array factory where factory[j] = [positionj, limitj] indicates that positionj is the position of the jth factory and that the jth factory can repair at most limitj robots.

The positions of each robot are unique. The positions of each factory are also unique. Note that a robot can be in the same position as a factory initially.

All the robots are initially broken; they keep moving in one direction. The direction could be the negative or the positive direction of the X-axis. When a robot reaches a factory that did not reach its limit, the factory repairs the robot, and it stops moving.

At any moment, you can set the initial direction of moving for some robot. Your target is to minimize the total distance traveled by all the robots.

Return the minimum total distance traveled by all the robots. The test cases are generated such that all the robots can be repaired.

Note that

All robots move at the same speed.
If two robots move in the same direction, they will never collide.
If two robots move in opposite directions and they meet at some point, they do not collide. They cross each other.
If a robot passes by a factory that reached its limits, it crosses it as if it does not exist.
If the robot moved from a position x to a position y, the distance it moved is |y - x|.

# dp with condition state of robot, facotry, limit used
"""


class Solution:
    def minimumTotalDistance(self, R: List[int], F: List[List[int]]) -> int:
        R.sort()
        F.sort()

        @lru_cache(None)
        def dp(i, j, k):
            # return the cost of fixing robot[i:] with F[i] already fixes k robots
            if i == len(R):
                # all robot has been fixed and cost = 0
                return 0
            if j == len(F):
                # all possible repairs are used up and cost = inf
                return float('inf')
            # 1. we do not fix i robot and other robots at j factory
            res1 = dp(i, j + 1, 0)
            # 2. we fix i robot at j factory
            res2 = dp(i + 1, j, k + 1) + abs(R[i] - F[j][0]) if F[j][1] > k else float('inf')
            return min(res1, res2)

        return dp(0, 0, 0)