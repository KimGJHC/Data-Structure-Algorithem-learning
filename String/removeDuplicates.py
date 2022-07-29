"""
1209. Remove All Adjacent Duplicates in String II

You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.
"""


class Solution:
    def removeDuplicates_v1(self, s, k):
        if not s:
            return s
        stack = []

        i = 0
        while i < len(s):
            if i == 0 or s[i] != s[i - 1]:
                stack.append(1)
            else:
                stack[-1] += 1
                if stack[-1] == k:
                    stack.pop()
                    s = s[:i - k + 1] + s[i + 1:]
                    i -= k
            i += 1
        return s

    def removeDuplicates(self, s, k):
        stack = [["@", 0]]

        for letter in s:
            if letter != stack[-1][0]:
                stack.append([letter, 1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
        return ''.join(letter*count for letter, count in stack)