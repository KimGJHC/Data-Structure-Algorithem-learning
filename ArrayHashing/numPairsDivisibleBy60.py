"""
1010. Pairs of Songs With Total Durations Divisible by 60

You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

"""
import math
class Solution:
    def numPairsDivisibleBy60(self, time):
        time_count = {}
        for t in time:
            t = t % 60
            time_count[t] = time_count.get(t, 0) + 1

        res = 0
        for t_i in time_count:
            if t_i in (0, 30):
                res += math.comb(time_count.get(t_i % 60, 0), 2)
            elif t_i < 6 0 -t_i:
                res += time_count[t_i] * time_count.get(6 0 -t_i, 0)
        return res