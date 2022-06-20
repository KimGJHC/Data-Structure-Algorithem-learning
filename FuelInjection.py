def helper(x):
    # return number of zeros on the right of binary representation of x
    return len(x) - len(x.rstrip('0'))

def solution(n):
    # The dp method seems not to work, I will consider a greedy method for now
    # Note that the early we use the /2 operation, the more pellet will be removed by the single operation,
    # therefore I greedily look for the earliest valid /2 operation,
    # A shortcut for find the number of /2 operation will be using bit operation
    n = int(n)
    count = 0

    while n > 1:
        # n = 3 is the special case that /2 operation does not remove more pellets than -1 operation
        if n == 3:
            count += 2
            break

        right_zero = helper(bin(n))

        if not right_zero:
            right_zero_up = helper(bin(n + 1))
            right_zero_down = helper(bin(n - 1))
            if right_zero_up > right_zero_down:
                n += 1
            else:
                n -= 1
            count += 1
        else:
            n = n >> right_zero
            count += right_zero

    return count
