"""
1604. Alert Using Same Key-Card Three or More Times in a One Hour Period

LeetCode company workers use key-cards to unlock office doors. Each time a worker uses their key-card, the security system saves the worker's name and the time when it was used. The system emits an alert if any worker uses the key-card three or more times in a one-hour period.

You are given a list of strings keyName and keyTime where [keyName[i], keyTime[i]] corresponds to a person's name and the time when their key-card was used in a single day.

Access times are given in the 24-hour time format "HH:MM", such as "23:51" and "09:49".

Return a list of unique worker names who received an alert for frequent keycard use. Sort the names in ascending order alphabetically.

Notice that "10:00" - "11:00" is considered to be within a one-hour period, while "22:51" - "23:52" is not considered to be within a one-hour period.
"""

import collections
class Solution:
    def alertNames(self, keyName, keyTime):

        name_time = collections.defaultdict(list)
        for i in range(len(keyName)):
            name_time[keyName[i]].append((int(keyTime[i][:2]), int(keyTime[i][-2:])))
        res = []

        for name in name_time:
            times = sorted(name_time[name], key=lambda x: (x[0], x[1]))
            n = len(times)
            if n < 3:
                break
            else:
                for i in range(n - 2):
                    t_h, t_m = times[i][0], times[i][1]
                    t2_h, t2_m = times[i + 2][0], times[i + 2][1]
                    if t2_h - t_h == 0:
                        res.append(name)
                        break
                    elif t2_h - t_h > 1:
                        continue
                    else:
                        if t2_m - t_m > 0:
                            continue
                        else:
                            res.append(name)
                            break
        return sorted(res)
# solution: seperate by name, sort time
# time: O(nlogn) where n = len(keyName)
# space: O(n)