def solution(l):
    n = len(l)
    if n <= 2:
        return 0

    # create table for valid 2 sum in l[i:]
    dp = [0] * n
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if l[j] % l[i] == 0:
                dp[i] += 1

    count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            if l[j] % l[i] == 0:
                count += dp[j]
    return count
