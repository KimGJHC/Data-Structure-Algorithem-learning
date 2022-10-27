"""
818. Race Car
Your car starts at position 0 and speed +1 on an infinite number line. Your car can go into negative positions. Your car drives automatically according to a sequence of instructions 'A' (accelerate) and 'R' (reverse):

When you get an instruction 'A', your car does the following:
position += speed
speed *= 2
When you get an instruction 'R', your car does the following:
If your speed is positive then speed = -1
otherwise speed = 1
Your position stays the same.
For example, after commands "AAR", your car goes to positions 0 --> 1 --> 3 --> 3, and your speed goes to 1 --> 2 --> 4 --> -1.

Given a target position target, return the length of the shortest sequence of instructions to get there.

1. looking for shortest distance => bfs
2. dp with consideration of 2**(n-1) -1 <= target < 2**n -1
"""


class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 0, 1)])  # moves, position, speed
        visited = set()

        while queue:
            moves, position, speed = queue.popleft()

            if position == target:
                return moves

            if (position, speed) in visited:
                continue
            else:
                visited.add((position, speed))
                # add A
                queue.append((moves + 1, position + speed, speed * 2))
                # add R
                if (position + speed > target and speed > 0) or (position + speed < target and speed < 0):
                    queue.append((moves + 1, position, 1 if speed < 0 else -1))

    dp = {0: 0}
    def racecar_v2(self, target: int) -> int:
        if target in self.dp:
            return self.dp[target]
        n = target.bit_length()
        if 2 ** n - 1 == target:
            self.dp[target] = n
        else:
            self.dp[target] = self.racecar_v2(2 ** n - 1 - target) + n + 1
            for m in range(n - 1):
                self.dp[target] = min(self.dp[target], self.racecar_v2(target - 2 ** (n-1) + 2**m) + n + m + 1)
        return self.dp[target]