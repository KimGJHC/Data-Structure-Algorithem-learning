"""
923. 3Sum With Multiplicity

Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 109 + 7.
"""


class Solution:
    def threeSumMulti(self, arr, target):
        MOD = 10 ** 9 + 7
        count = 0

        # O(nlogn)
        arr.sort()

        n = len(arr)

        # O(n)
        for i in range(n - 2):
            num = arr[i]
            twoSumTarget = target - num
            j, k = i + 1, n - 1

            # O(n-i)
            while j < k:
                if arr[j] + arr[k] < twoSumTarget:
                    j += 1
                elif arr[j] + arr[k] > twoSumTarget:
                    k -= 1
                elif arr[j] != arr[k]:
                    count_j, count_k = 1, 1
                    while j + 1 < k and arr[j] == arr[j + 1]:
                        count_j += 1
                        j += 1
                    while j <= k and arr[k] == arr[k - 1]:
                        count_k += 1
                        k -= 1
                    count += count_j * count_k
                    count %= MOD
                    j += 1
                    k -= 1
                else:
                    count_j_k = k - j + 1
                    count += count_j_k * (count_j_k - 1) // 2
                    count %= MOD
                    j = k
        return count

# solution 1: fix i and count j, k, using 2 pointers on sorted array
# time: O(n**2)
# space: O(1)

        def threeSumMulti_v2(self, arr, target):
            import collections
            MOD = 10 ** 9 + 7
            count = 0

            arr_count = collections.Counter(arr)
            keys = sorted(arr_count)
            n = len(keys)

            for i, x in enumerate(keys):
                T = target - x
                j, k = i, n - 1
                while j <= k:
                    y, z = keys[j], keys[k]
                    if y + z < T:
                        j += 1
                    elif y + z > T:
                        k -= 1
                    else:
                        if i < j < k:
                            count += arr_count[x] * arr_count[y] * arr_count[z]
                        elif i == j < k:
                            count += arr_count[x] * (arr_count[x] - 1) // 2 * arr_count[z]
                        elif i < j == k:
                            count += arr_count[y] * (arr_count[y] - 1) // 2 * arr_count[x]
                        else:
                            count += arr_count[x] * (arr_count[x] - 1) * (arr_count[x] - 2) // 6
                        j += 1
                        k -= 1
            return count % MOD

# solution 2: count

