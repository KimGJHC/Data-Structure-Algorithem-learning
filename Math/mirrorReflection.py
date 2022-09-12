"""
858. Mirror Reflection

There is a special square room with mirrors on each of the four walls. Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

The square room has walls of length p and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

Given the two integers p and q, return the number of the receptor that the ray meets first.

The test cases are guaranteed so that the ray will meet a receptor eventually.

"""
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        k = 1
        while q*k % p:
            k += 1
        val = (q * k // p) % 2
        if k % 2 == 0 and val == 1:
            return 2
        elif k % 2 == 1:
            if val == 1:
                return 1
            else:
                return 0