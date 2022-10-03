"""
1868. Product of Two Run-Length Encoded Arrays
Run-length encoding is a compression algorithm that allows for an integer array nums with many segments of consecutive repeated numbers to be represented by a (generally smaller) 2D array encoded. Each encoded[i] = [vali, freqi] describes the ith segment of repeated numbers in nums where vali is the value that is repeated freqi times.

For example, nums = [1,1,1,2,2,2,2,2] is represented by the run-length encoded array encoded = [[1,3],[2,5]]. Another way to read this is "three 1's followed by five 2's".
The product of two run-length encoded arrays encoded1 and encoded2 can be calculated using the following steps:

Expand both encoded1 and encoded2 into the full arrays nums1 and nums2 respectively.
Create a new array prodNums of length nums1.length and set prodNums[i] = nums1[i] * nums2[i].
Compress prodNums into a run-length encoded array and return it.
You are given two run-length encoded arrays encoded1 and encoded2 representing full arrays nums1 and nums2 respectively. Both nums1 and nums2 have the same length. Each encoded1[i] = [vali, freqi] describes the ith segment of nums1, and each encoded2[j] = [valj, freqj] describes the jth segment of nums2.

Return the product of encoded1 and encoded2.

Note: Compression should be done such that the run-length encoded array has the minimum possible length.
"""


class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        res = []
        q1 = deque(encoded1)
        q2 = deque(encoded2)
        cur1 = None
        cur2 = None

        while q1 or q2:
            if not cur1:
                cur1 = q1.popleft()
            if not cur2:
                cur2 = q2.popleft()

            minLen = min(cur1[1], cur2[1])
            candidate = [cur1[0] * cur2[0], minLen]
            if res and res[-1][0] == candidate[0]:
                res[-1][1] += minLen
            else:
                res.append(candidate)

            cur1[1] -= minLen
            cur2[1] -= minLen

            if cur1[1] == 0:
                cur1 = None
            if cur2[1] == 0:
                cur2 = None

        return res