"""
647. Palindromic Substrings

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Input: s = "abc"
Output: 3

Input: s = "aaa"
Output: 6
"""

def countSubstrings(s):
    # The idea is to consider each of the letter to be middle of a palindrome and expand on two side if possible
    # This is not actually DP

    count = 0
    n = len(s)

    if not n:
        return 0

    for palindrome_middle in range(n):
        # odd case
        l , r = palindrome_middle, palindrome_middle
        while 0 <= l and r < n and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        # even case
        l, r = palindrome_middle, palindrome_middle+1
        while 0 <= l and r < n and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
    return count

# time: O(n^2)
# space: O(1)



def test():
    assert countSubstrings("abc") == 3
    assert countSubstrings("aaa") == 6
    print("All tests passed!")
