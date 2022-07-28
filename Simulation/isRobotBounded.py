"""
1041. Robot Bounded In Circle

On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:

The north direction is the positive direction of the y-axis.
The south direction is the negative direction of the y-axis.
The east direction is the positive direction of the x-axis.
The west direction is the negative direction of the x-axis.
The robot can receive one of three instructions:

"G": go straight 1 unit.
"L": turn 90 degrees to the left (i.e., anti-clockwise direction).
"R": turn 90 degrees to the right (i.e., clockwise direction).
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

"""
# The key here is to understand the circle path and divergent path

class Solution:
    def __init__(self):
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # initially we have directions[0]

    def isRobotBounded(self, instructions):
        position, direction = self.execute([0, 0], 0, instructions)
        if position == [0, 0] or direction != 0:
            return True
        return False

    def execute(self, position, direction, instructions):
        # return position and direction of element after one iteration of instructions
        # direction will be 0, 1, 2, 3 in terms of directions

        for move in instructions:
            if move == 'G':
                position[0] += self.directions[direction][0]
                position[1] += self.directions[direction][1]
            elif move == 'L':
                direction = (direction + 3) % 4
            else:  # R
                direction = (direction + 1) % 4
        return position, direction

# time: O(n)
# space: O(1)