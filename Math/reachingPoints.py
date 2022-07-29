"""
780. Reaching Points

Given four integers sx, sy, tx, and ty, return true if it is possible to convert the point (sx, sy) to the point (tx, ty) through some operations, or false otherwise.

The allowed operation on some point (x, y) is to convert it to either (x, x + y) or (x + y, y).
"""

def reachingPoints(sx, sy, tx, ty):
    while tx >= sx and ty >= sy:
        if tx == ty:
            break
        elif tx > ty:
            if ty > sy:
                tx %= ty
            elif ty == sy:
                return (tx - sx) % ty == 0
            else:
                return False
        else:
            if tx > sx:
                ty %= tx
            elif tx == sx:
                return (ty - sy) % tx == 0
            else:
                return False
    return tx == sx and ty == sy