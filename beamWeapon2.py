from itertools import product
from math import atan2


def solution(dimensions, your_position, trainer_position, distance):
    x0, y0 = your_position
    hits = dict()

    for position in your_position, trainer_position:
        # reflect is defined on number of reflection on the 2 dimensions
        for reflect in product(*[range(-(distance // -d) + 1) for d in dimensions]):
            # quadrant is used to distinguish the directions of reflection (1 dimensions have 2 directions)
            for quadrant in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
                x, y = [(d * r + (d - p if r % 2 == 1 else p)) * q
                    for d, p, r, q in zip(dimensions, position, reflect, quadrant)]
                # compute travelled distance
                travel = (abs(x - x0) ** 2 + abs(y - y0) ** 2) ** 0.5
                # compute the angle
                angle = atan2(x0 - x, y0 - y)
                # if travelled distance is larger than distance
                # or the angle will hit yourself and travelled distance is larger than the distance for hitting yourself
                # we are not able to hit the target
                if travel > distance or (angle in hits and travel > abs(hits[angle])):
                    continue
                else:
                    hits[angle] = travel * (-1 if position == your_position else 1)
    return sum([val > 0 for val in hits.values()])
