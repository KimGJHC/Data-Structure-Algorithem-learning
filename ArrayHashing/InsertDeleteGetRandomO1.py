"""
380. Insert Delete GetRandom O(1)
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

1. insert, getrandom O(1) => array, delete (find) O(1) => set
"""


class RandomizedSet:

    def __init__(self):
        self.size = 0
        self.nums = []
        self.val_to_idx = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False
        else:
            self.nums.append(val)
            self.val_to_idx[val] = self.size
            self.size += 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.val_to_idx:
            idx_pop = self.val_to_idx[val]
            self.nums[idx_pop], self.nums[-1] = self.nums[-1], self.nums[idx_pop]
            self.val_to_idx[self.nums[idx_pop]] = idx_pop
            self.nums.pop()
            self.val_to_idx.pop(val)
            self.size -= 1
            return True
        else:
            return False

    def getRandom(self) -> int:
        return self.nums[random.randint(0, self.size - 1)]