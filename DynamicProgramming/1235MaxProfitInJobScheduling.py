"""
1235. Maximum Profit in Job Scheduling
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

# For questions scheduling time intervals, we usually want to sort by start or end time
# here we sort by start time so that when we take one job, we can use binary search to find the next valid job
# use top-down dp here
"""


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort(key=lambda x: x[0])
        startTime = [s for s, _, _ in jobs]
        n = len(startTime)

        def findNextJob(lastEnd):
            # get the index of the first start time after last end
            start = 0
            end = n - 1
            res = n

            while start <= end:
                mid = (start + end) // 2
                if (startTime[mid] >= lastEnd):
                    res = mid
                    end = mid - 1
                else:
                    start = mid + 1
            return res

        @lru_cache(None)
        def dp(i):
            # maximum profit we can obatin from jobs[i:]
            if i == n:
                return 0

            res = max(dp(i + 1), jobs[i][2] + dp(findNextJob(jobs[i][1])))

            return res

        return dp(0)

