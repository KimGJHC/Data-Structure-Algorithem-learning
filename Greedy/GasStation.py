"""
134. Gas Station

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
"""

def canCompleteCycle(gas, cost):
    n = len(gas)
    start = 0

    while start < n:
        gas_tank = 0
        step = 0
        while step < n:
            if gas_tank + gas[(start + step) % n] >= cost[(start + step) % n]:
                gas_tank += gas[(start + step) % n] - cost[(start + step) % n]
                step += 1
            else:
                break
        if step == n:
            return start
        else:
            start += step + 1
    return -1

# time: O(n)
# space: O(1)

def test():
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    assert canCompleteCycle(gas, cost) == 3
    gas = [2,3,4]
    cost = [3,4,3]
    assert canCompleteCycle(gas, cost) == -1
    print("All tests passed!")



