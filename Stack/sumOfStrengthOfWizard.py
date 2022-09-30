"""
2281. Sum of Total Strength of Wizards

As the ruler of a kingdom, you have an army of wizards at your command.

You are given a 0-indexed integer array strength, where strength[i] denotes the strength of the ith wizard. For a contiguous group of wizards (i.e. the wizards' strengths form a subarray of strength), the total strength is defined as the product of the following two values:

The strength of the weakest wizard in the group.
The total of all the individual strengths of the wizards in the group.
Return the sum of the total strengths of all contiguous groups of wizards. Since the answer may be very large, return it modulo 109 + 7.

A subarray is a contiguous non-empty sequence of elements within an array.
"""


class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        n = len(strength)
        mod = 10 ** 9 + 7

        # for each strength[i], find [i - l + 1 to i + r - 1 inclusive]
        # s.t. len_l[i] is the leftmost occurence of minimum
        len_l = [0] * n
        len_r = [0] * n
        stk = []

        for i in range(n - 1, -1, -1):
            while stk and strength[stk[-1]] >= strength[i]:
                j = stk.pop()
                len_l[j] = j - i
            stk.append(i)
        for j in stk:
            len_l[j] = j + 1

        for i in range(n):
            while stk and strength[stk[-1]] > strength[i]:
                j = stk.pop()
                len_r[j] = i - j
            stk.append(i)
        for j in stk:
            len_r[j] = n - j

        # prefix sum of prefix sum
        psps = list(accumulate(accumulate(strength))) + [0]

        ans = 0
        for i in range(n):
            L = len_l[i]
            R = len_r[i]
            total_R = (psps[i + R - 1] - psps[i - 1]) * L
            total_L = (psps[i - 1] - psps[max(-1, i - L - 1)]) * R
            ans = (ans + strength[i] * (total_R - total_L)) % mod
        return ans
