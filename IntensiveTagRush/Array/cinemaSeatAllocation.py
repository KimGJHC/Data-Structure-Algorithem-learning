"""
1386. Cinema Seat Allocation
A cinema has n rows of seats, numbered from 1 to n and there are ten seats in each row, labelled from 1 to 10 as shown in the figure above.

Given the array reservedSeats containing the numbers of seats already reserved, for example, reservedSeats[i] = [3,8] means the seat located in row 3 and labelled with 8 is already reserved.

Return the maximum number of four-person groups you can assign on the cinema seats. A four-person group occupies four adjacent seats in one single row. Seats across an aisle (such as [3,3] and [3,4]) are not considered to be adjacent, but there is an exceptional case on which an aisle split a four-person group, in that case, the aisle split a four-person group in the middle, which means to have two people on each side.
"""

import heapq
class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        self.memo = {}

        res = 0
        heapq.heapify(reservedSeats)

        for row_number in range(1, n + 1):
            row = [0] * 10
            while reservedSeats and reservedSeats[0][0] == row_number:
                _, col_number = heapq.heappop(reservedSeats)
                row[col_number - 1] = 1

            empty23 = row[1] + row[2] == 0
            empty45 = row[3] + row[4] == 0
            empty67 = row[5] + row[6] == 0
            empty89 = row[7] + row[8] == 0

            state = (empty23, empty45, empty67, empty89)
            res += self.getPlacementNumber(state)

        return res

    def getPlacementNumber(self, state):
        if state not in self.memo:
            empty23, empty45, empty67, empty89 = state
            if not empty45:
                if empty67 and empty89:
                    self.memo[state] = 1
                else:
                    self.memo[state] = 0
            elif not empty67:
                if empty23 and empty45:
                    self.memo[state] = 1
                else:
                    self.memo[state] = 0
            else:
                if empty23 and empty89:
                    self.memo[state] = 2
                else:
                    self.memo[state] = 1

        return self.memo[state]

# time complexity is too high because of sorting, lets use bitmask
    def maxNumberOfFamilies_v2(self, n, reservedSeats):
        row_state = [0] * n
        for row_number, col_number in reservedSeats:
            if col_number in [2, 3]:
                row_state[row_number - 1] |= 1
            elif col_number in [4, 5]:
                row_state[row_number - 1] |= 1 << 1
            elif col_number in [6, 7]:
                row_state[row_number - 1] |= 1 << 2
            elif col_number in [8, 9]:
                row_state[row_number - 1] |= 1 << 3

        memo = {0: 2, 1: 1, 2: 1, 3: 1, 4: 1, 5: 0, 6: 0, 7: 0, 8: 1, 9: 1, 10: 0, 11: 0, 12: 1, 13: 0, 14: 0, 15: 0}
        res = 0

        for state in row_state:
            res += memo[state]
        return res


    def maxNumberOfFamilies_v3(self, n, reservedSeats):
        import collections
        seats = collections.defaultdict(set)
        for i, j in reservedSeats:
            if j in [2, 3, 4, 5]:
                seats[i].add(0)
            if j in [4, 5, 6, 7]:
                seats[i].add(1)
            if j in [6, 7, 8, 9]:
                seats[i].add(2)
        res = 2 * n
        for i in seats:
            if len(seats[i]) == 3:
                res -= 2
            else:
                res -= 1
        return res

# time: O(n)
# space: O(n)