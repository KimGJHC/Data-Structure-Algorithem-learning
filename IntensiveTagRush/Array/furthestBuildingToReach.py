"""
1642. Furthest Building You Can Reach
You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.
"""

import bisect
class Solution:
    def furthestBuilding(self, heights, bricks, ladders):
        height_diff = [(heights[i] - heights[i - 1], i) for i in range(1, len(heights))]
        height_diff = [diff for diff in height_diff if diff[0] > 0]

        if len(height_diff) <= ladders:
            return len(heights) - 1

        diff = [h for h, _ in height_diff[:ladders]]
        diff.sort()
        i = ladders

        while i < len(height_diff):
            new_height, idx = height_diff[i]
            diff_idx = bisect.bisect_left(diff, new_height)
            if diff_idx == len(diff):
                diff.append(new_height)
            else:
                diff = diff[:diff_idx] + [new_height] + diff[diff_idx:]
            # check if enough bricks
            if sum(diff[:len(diff) - ladders]) > bricks:
                break
            i += 1

        if i < len(height_diff):
            return height_diff[i][1] - 1
        else:
            return len(heights) - 1

# time: O(n**2)
    def furthestBuilding_v2(self, heights, bricks, ladders):
        import heapq
        height_for_ladder = []
        bricks_needed = 0

        for i in range(1, len(heights)):
            height_diff = heights[i] - heights[i - 1]
            if height_diff <= 0:
                continue
            else:
                heapq.heappush(height_for_ladder, height_diff)
                while len(height_for_ladder) > ladders:
                    bricks_needed += heapq.heappop(height_for_ladder)

                if bricks_needed > bricks:
                    return i - 1
        return len(heights) - 1
# solution: minheap + greedy
# time: O(n log ladder) for n = len(heights)
# space: O(ladder)
