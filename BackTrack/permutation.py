"""
46. Permutations
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(candidates, path=[]):
            nonlocal res
            if len(path) == n:
                res.append(path[:])
                return
            else:
                for candidate in candidates.copy():
                    path.append(candidate)
                    candidates.remove(candidate)
                    backtrack(candidates, path)
                    candidates.add(path.pop())

        backtrack(set(nums))
        return res