"""
2024. Maximize the Confusion of an Exam
A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).

You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:

Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.

# sliding window and track number of T and F in the window, we will always keep the window valid by track the min(T, F)
# (the window is valid as long as min(T, F) <= k)
# Note that the size of the sliding window is monotonically increasing
"""


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l = 0
        memo = {'T': 0, 'F': 0}

        for r, ans in enumerate(list(answerKey)):
            memo[ans] += 1

            if min(memo.values()) > k:
                memo[answerKey[l]] -= 1
                l += 1
        return r - l + 1