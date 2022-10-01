"""
39. Combination Sum
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        def backtrack(first, target, path, path_sum):
            nonlocal res
            if path_sum > target:
                return
            elif path_sum == target:
                res.append(path[:])
                return
            else:
                for i in range(first, n):
                    path.append(candidates[i])
                    path_sum += candidates[i]
                    backtrack(i, target, path, path_sum)
                    path_sum -= path.pop()
        backtrack(0, target, [], 0)
        return res