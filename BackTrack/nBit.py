import math

def graycode(n):
    res = [0]
    used = {0}
    need, count = 2 ** n, 1

    def backtrack(prev):
        # prev is an int
        nonlocal res
        nonlocal count
        nonlocal need

        if count == need - 1:
            for i in range(n):
                val = prev ^ (1 << i)
                if val in used:
                    continue
                num = 1
                for i in range(n):
                    if num == val:
                        res.append(val)
                        return True
                    num = num << 1
        for i in range(n):
            val = prev ^ (1 << i)
            if val in used:
                continue
            res.append(val)
            count += 1
            used.add(val)
            if backtrack(val):
                return True
            res.pop()
            count -= 1
            used.remove(val)

        return False

    backtrack(0)
    return res


def grayCode2(n):
    res = [0]
    for i in range(1, 2 ** n):
        res.append(res[-1] ^ (i & -i))
    return res
