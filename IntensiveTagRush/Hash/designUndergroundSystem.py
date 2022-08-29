"""
1396. Design Underground System
An underground railway system is keeping track of customer travel times between different stations. They are using this data to calculate the average time it takes to travel from one station to another.

Implement the UndergroundSystem class:

void checkIn(int id, string stationName, int t)
A customer with a card ID equal to id, checks in at the station stationName at time t.
A customer can only be checked into one place at a time.
void checkOut(int id, string stationName, int t)
A customer with a card ID equal to id, checks out from the station stationName at time t.
double getAverageTime(string startStation, string endStation)
Returns the average time it takes to travel from startStation to endStation.
The average time is computed from all the previous traveling times from startStation to endStation that happened directly, meaning a check in at startStation followed by a check out from endStation.
The time it takes to travel from startStation to endStation may be different from the time it takes to travel from endStation to startStation.
There will be at least one customer that has traveled from startStation to endStation before getAverageTime is called.
You may assume all calls to the checkIn and checkOut methods are consistent. If a customer checks in at time t1 then checks out at time t2, then t1 < t2. All events happen in chronological order.
"""


class UndergroundSystem:

    def __init__(self):
        self.travel_time = {}  # {(src, dest): [total, count]}
        self.traveller = {}  # {id: [start, t]}

    def checkIn(self, id: int, stationName: str, t: int) -> None: # O(1)
        self.traveller[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None: # O(1)
        src, start_time = self.traveller[id]
        travel = (src, stationName)
        if travel not in self.travel_time:
            self.travel_time[travel] = [t - start_time, 1]
        else:
            self.travel_time[travel][0] += t - start_time
            self.travel_time[travel][1] += 1

        self.traveller.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float: # O(1)
        travel = (startStation, endStation)
        total_time, freq = self.travel_time[travel]
        return total_time / freq

