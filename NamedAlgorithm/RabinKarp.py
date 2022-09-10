"""
This is for pattern searching:

Given a string s and a pattern p, search all occurances of p in s. (Assume len(s) > len(p))

We will use the rolling hash method.
"""
import string


def rabinKarp(s, p):
    MOD = 10**9 + 7
    prime = 113
    len_p = len(p)
    len_s = len(s)

    p_hash = 0
    s_hash = 0
    # compute p hash
    for i, char in enumerate(p):
        p_hash += (ord(char)) * prime ** (len_p-1-i)
    p_hash %= MOD

    # try to find p hash in s
    pattern_match_position = []
    for i in range(len_p):
        s_hash += (ord(s[i])) * prime ** (len_p - 1 - i)
    s_hash %= MOD
    if s_hash == p_hash:
        pattern_match_position.append(0)

    for j in range(len_p, len_s):
        s_next = s[j]
        s_hash = (s_hash - (ord(s[j-len_p])) * prime ** (len_p-1)) * prime + (ord(s_next)) % MOD
        if s_hash == p_hash:
            pattern_match_position.append(j - len_p+1)
    return pattern_match_position


