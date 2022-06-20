from math import sqrt

def solution(dimensions, your_position, trainer_position, distance):
    if distance <= dist(your_position, trainer_position):
        return 0

    x_me, y_me = your_position

    # get pool1 of direction candidates that can hit the target

    # 1. get positions of reflected target within distance
    reflectedTarget = getAllReflected(dimensions, your_position, trainer_position, distance)
    # 2. convert target position to direction
    directionPool = [[x - x_me, y - y_me] for x, y in reflectedTarget]
    # 3. get rid of same direction by keeping only the smaller
    directionPool = refineDirection(directionPool)

    # get pool2 of direction candidates that can hit myself

    # 1. get positions of reflected myself within distance
    reflectedMe = getAllReflected(dimensions, your_position, your_position, distance)
    directionToMe = [[x - x_me, y - y_me] for x, y in reflectedMe if x != your_position[0] or y != your_position[1]]

    # based on pool1 and pool2 get direction that can hit the target but none of pool2 in trajectory
    count = 0
    for d in directionPool:
        if isValid(d, directionToMe):
            count += 1

    return count


def getAllReflected(dimension, dist_position, position, distance):
    # return all the possible reflected positions within distance from dist_position
    w, h = dimension
    x, y = position

    visited = {(x, y)}
    queue = [(x, y)]
    while queue:
        current = queue.pop(0)
        x_current, y_current = current
        neighbors = [(x_current, -y_current), (-x_current, y_current), (x_current, 2 * h - y_current), (2 * w - x_current, y_current)]
        for neig in neighbors:
            if neig not in visited and dist(dist_position, neig) <= distance:
                visited.add(neig)
                queue.append(neig)
    return list(visited)


def dist(position1, position2):
    # return distance between two positions
    return sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)


def isValid(d, directionToMe):
    # True if for reach direction in directionToMe, d and direction is not in same direction or vector length(d) <
    # length(direction)
    if d[0] == 0:
        for direct in directionToMe:
            if direct[0] == 0 and abs(direct[1]) < abs(d[1]):
                return False
    elif d[1] == 0:
        for direct in directionToMe:
            if direct[1] == 0 and abs(direct[0]) < abs(d[0]):
                return False
    else:
        for direct in directionToMe:
            if direct[0] / d[0] == direct[1] / d[1] and abs(direct[0]) < abs(d[0]):
                return False
    return True

def refineDirection(direction):
    res = set()
    xeq0_direction1 = [y for x, y in direction if x == 0 and y < 0]
    xeq0_direction2 = [y for x, y in direction if x == 0 and y > 0]
    yeq0_direction1 = [x for x, y in direction if y == 0 and x < 0]
    yeq0_direction2 = [x for x, y in direction if y == 0 and x > 0]

    if len(xeq0_direction1) > 0:
        res.add((0, max(xeq0_direction1)))
    if len(xeq0_direction2) > 0:
        res.add((0, min(xeq0_direction2)))
    if len(yeq0_direction1) > 0:
        res.add((max(yeq0_direction1), 0))
    if len(yeq0_direction2) > 0:
        res.add((min(yeq0_direction2), 0))

    for d in direction:
        if d[0] != 0 and d[1] != 0:
            gcd_ = gcd(d[0], d[1])
            x_new, y_new = d[0]//gcd_, d[1]//gcd_
            res.add((x_new, y_new))

    return list(res)

def gcd(a, b):
    while b:
        a, b = b, a%b
    return abs(a)