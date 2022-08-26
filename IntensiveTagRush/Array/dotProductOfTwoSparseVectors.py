"""
1570. Dot Product of Two Sparse Vectors
Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?
"""


class SparseVector:
    def __init__(self, nums):
        self.items = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.items[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        res = 0
        all_idx = set()
        for idx in self.items.keys():
            all_idx.add(idx)

        for idx in vec.items.keys():
            all_idx.add(idx)

        for idx in all_idx:
            if idx in self.items and idx in vec.items:
                res += self.items[idx] * vec.items[idx]
        return res

# time: O(n) where n = len(nums) for dotProduct for worse case
# space: O(1)