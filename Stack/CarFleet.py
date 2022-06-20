def numFleet(target, position, speed):
    distance = [12 - p for p in position]
    cars = zip(distance, speed)
    cars = sorted(cars, key = lambda x: x[0])
    times = [car[0]/car[1] for car in cars]
    time_max = -float("inf")
    count = 0
    for t in times:
        if t > time_max:
            count += 1
            time_max = t
    return count
