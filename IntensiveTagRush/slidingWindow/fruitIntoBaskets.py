"""
904. Fruit Into Baskets
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.
"""

import collections
class Solution:
    def totalFruit(self, fruits):
        max_fruits = 0
        last_fruit_indices = {}
        queue = collections.deque()

        for i, fruit in enumerate(fruits):
            if len(last_fruit_indices) < 2 or fruit in last_fruit_indices:
                last_fruit_indices[fruit] = i
                queue.append(fruit)
            else:
                recent_fruit, recent_fruit_idx = -1, -1
                for old_fruit, recent_idx in last_fruit_indices.items():
                    if recent_idx > recent_fruit_idx:
                        recent_fruit_idx = recent_idx
                        recent_fruit = old_fruit

                new_queue = collections.deque()
                while queue[-1] == recent_fruit:
                    new_queue.append(queue.pop())
                new_queue.append(fruit)

                last_fruit_indices = {recent_fruit: recent_fruit_idx, fruit: i}

                queue = new_queue

            max_fruits = max(max_fruits, len(queue))
        return max_fruits

# time: O(n)
# space: O(n)

    def totalFruit_v2(self, fruits):
        l = 0
        res = 0
        count = collections.Counter()

        for r in range(len(fruits)):
            count[fruits[r]] += 1
            while len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    count.pop(fruits[l])
                l += 1
            res = max(res, sum(count.values()))
        return res