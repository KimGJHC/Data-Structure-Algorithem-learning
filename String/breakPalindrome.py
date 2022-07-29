"""
1328. Break a Palindrome

Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.

Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.
"""
def breakPalindrome_v1(palindrome):
    n = len(palindrome)

    if n <= 1:
        return ""

    if n % 2 == 0:
        for i in range(n):
            if palindrome[i] > 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]
    else:
        mid = n // 2
        for i in range(n):
            if i == mid:
                continue
            if palindrome[i] > 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]
    return palindrome[:-1] + 'b'

# time: O(n), n is the size of palindrome
# space: O(n)

def breakPalindrome(palindrome):
    n = len(palindrome)

    if n <= 1:
        return ""

    mid = n // 2

    for i in range(mid):
        if palindrome[i] > 'a':
            return palindrome[:i] + 'a' + palindrome[i + 1:]

    return palindrome[:-1] + 'b'

# optimized time by not looking at index after mid
# asyn time complexity not changed