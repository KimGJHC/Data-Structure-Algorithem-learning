"""
735. Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Input: asteroids = [5,10,-5]
Output: [5,10]

Input: asteroids = [8,-8]
Output: []

Input: asteroids = [10,2,-5]
Output: [10]
"""

def asteroidCollision(asteroids):
    # we will use a stack to preserve the order and keep comparing left and right sizes
    res = []
    positive_stack = [] # only stores ast to right

    for asteroid in asteroids:
        if not positive_stack:
            if asteroid < 0:
                res.append(asteroid)
            else:
                positive_stack.append(asteroid)
        else:
            if asteroid > 0:
                positive_stack.append(asteroid)
            else:
                while positive_stack:
                    if positive_stack[-1] > -asteroid:
                        break
                    elif positive_stack[-1] == -asteroid:
                        positive_stack.pop()
                        asteroid = 0
                        break
                    else:
                        positive_stack.pop()
                if not positive_stack and asteroid != 0:
                    res.append(asteroid)
    res += positive_stack
    return res

# time: O(n)
# space: O(n)

def test():
    asteroids = [5, 10, -5]
    # assert asteroidCollision(asteroids) == [5, 10]
    asteroids = [8,-8]
    assert asteroidCollision(asteroids) == []
    asteroids = [1,-2,1,-1]
    assert asteroidCollision(asteroids) == [-2]
    print("All tests passed!")

