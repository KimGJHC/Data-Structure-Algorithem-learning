"""
1220. Count Vowels Permutation

Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.
"""


class Solution:
    def countVowelPermutation(self, n):
        previous = [1] * 5  # stores number of strings end with corresponding vowels
        current = [0] * 5
        a, e, i, o, u = 0, 1, 2, 3, 4
        MOD = 10 ** 9 + 7

        count = 1
        while count < n:
            current[0] = (previous[e] + previous[i] + previous[u]) % MOD
            current[1] = (previous[a] + previous[i]) % MOD
            current[2] = (previous[e] + previous[o]) % MOD
            current[3] = previous[i]
            current[4] = (previous[i] + previous[o]) % MOD

            count += 1
            previous = current.copy()
        return sum(previous) % MOD


# time: O(n)
# space: O(1)