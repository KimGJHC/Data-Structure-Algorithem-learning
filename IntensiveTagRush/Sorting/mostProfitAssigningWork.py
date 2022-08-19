"""
826. Most Profit Assigning Work
You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
Return the maximum profit we can achieve after assigning the workers to the jobs.
"""


class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker) -> int:
        works = list(zip(profit, difficulty))

        works.sort()
        worker.sort()

        total_profit = 0
        current_work = works.pop()
        while worker:
            current_worker = worker.pop()
            if current_worker >= current_work[1]:
                total_profit += current_work[0]
            else:
                while works and current_worker < current_work[1]:
                    current_work = works.pop()
                if current_worker < current_work[1]:
                    break
                else:
                    total_profit += current_work[0]
        return total_profit
# time: O(nlogn) where n = max(len(profit), len(worker))
# space: O(n)