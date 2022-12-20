"""
841. Keys and Rooms
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

# think about the question as graph and use bfs
# whenever we use set to access existence of element, we can probably use bitmasking to reduce runtime and memory consumption
"""

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)

        queue = collections.deque([0])
        visited = set()

        while queue:
            for i in range(len(queue)):
                current = queue.popleft()
                visited.add(current)

                for key in rooms[current]:
                    if key not in visited:
                        queue.append(key)
            if len(visited) == n:
                return True
        return False

    def canVisitAllRooms_v2(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        total = 2 ** n - 1
        queue = collections.deque([0])
        visited = 0
        # 0 means room is not being visited
        visited |= 1 << 0

        while queue:
            for i in range(len(queue)):
                current = queue.popleft()

                for key in rooms[current]:
                    if visited & (1 << key) == 0:
                        visited |= 1 << key
                        queue.append(key)
            if visited == total:
                return True
        return False