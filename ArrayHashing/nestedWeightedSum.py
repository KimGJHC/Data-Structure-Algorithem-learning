"""
339. Nested List Weight Sum
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

Return the sum of each integer in nestedList multiplied by its depth.
"""

import collections
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        queue = collections.deque(nestedList)
        depth = 0
        res = 0

        while queue:
            depth += 1
            for i in range(len(queue)):
                current = queue.popleft()
                value = current.getInteger()

                if value != None:
                    res += value * depth
                else:
                    queue += current.getList()
        return res
