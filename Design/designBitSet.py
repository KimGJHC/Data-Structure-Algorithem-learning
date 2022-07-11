"""
2166. Design Bitset

A Bitset is a data structure that compactly stores bits.

Implement the Bitset class:

Bitset(int size) Initializes the Bitset with size bits, all of which are 0.
void fix(int idx) Updates the value of the bit at the index idx to 1. If the value was already 1, no change occurs.
void unfix(int idx) Updates the value of the bit at the index idx to 0. If the value was already 0, no change occurs.
void flip() Flips the values of each bit in the Bitset. In other words, all bits with value 0 will now have value 1 and vice versa.
boolean all() Checks if the value of each bit in the Bitset is 1. Returns true if it satisfies the condition, false otherwise.
boolean one() Checks if there is at least one bit in the Bitset with value 1. Returns true if it satisfies the condition, false otherwise.
int count() Returns the total number of bits in the Bitset which have value 1.
String toString() Returns the current composition of the Bitset. Note that in the resultant string, the character at the ith index should coincide with the value at the ith bit of the Bitset.

"""


class Bitset:

    def __init__(self, size: int):
        self.num = 0
        self.size = size
        self.cnt = 0

    def fix(self, idx):
        if self.num & (1 << idx) == 0:
            self.num |= 1 << idx
            self.cnt += 1

    def unfix(self, idx):
        if self.num & (1 << idx):
            self.num ^= 1 << idx
            self.cnt -= 1

    def flip(self):
        self.num ^= (1 << self.size) - 1
        self.cnt = self.size - self.cnt

    def all(self):
        return self.cnt == self.size

    def one(self):
        return self.num > 0

    def count(self):
        return self.cnt

    def toString(self):
        res = bin(self.num)[2:]
        # be careful about the index and bit relation
        return res[::-1] + '0'*(self.size - len(res))

# time: O(1) except for toString
# space: O(1) except for to String

def test():
    obj = Bitset(5)
    obj.fix(3)
    obj.fix(1)
    obj.flip()
    assert obj.all() == False
    obj.unfix(0)
    obj.flip()
    assert obj.one() == True
    obj.unfix(0)
    assert obj.count == 2
    assert obj.toString() == '01010'
    print("All tests passed!")