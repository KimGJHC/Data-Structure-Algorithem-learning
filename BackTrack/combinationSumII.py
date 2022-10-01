"""
40. Combination Sum II
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        n = len(candidates)

        def backtrack(first, path_sum, path):
            nonlocal res
            if path_sum > target:
                return
            elif path_sum == target:
                res.append(path[:])
                return
            else:
                prev = -1
                for i in range(first, n):
                    if candidates[i] == prev:
                        continue
                    path.append(candidates[i])
                    path_sum += candidates[i]
                    backtrack(i + 1, path_sum, path)
                    path_sum -= path.pop()

                    prev = candidates[i]

        backtrack(0, 0, [])
        return res