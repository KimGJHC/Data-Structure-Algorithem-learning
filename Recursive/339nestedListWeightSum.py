"""
339. Nested List Weight Sum
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

Return the sum of each integer in nestedList multiplied by its depth.

simple recursive solution
"""


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        self.weight_sum = 0
        for nInteger in nestedList:
            self.depthSumNestedInteger(nInteger, 1)
        return self.weight_sum

    def depthSumNestedInteger(self, nestedInteger, depth):
        if nestedInteger.isInteger():
            self.weight_sum += depth * nestedInteger.getInteger()
        else:
            nestedList = nestedInteger.getList()
            for nInteger in nestedList:
                self.depthSumNestedInteger(nInteger, depth + 1)