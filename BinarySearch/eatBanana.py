class Solution:
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)

        while l < r:
            mid = (l + r) // 2
            if self.isValid(piles, h, mid):
                r = mid
            else:
                l = mid + 1
        return r

    def isValid(self, piles, h, k):
        hour_need = sum([math.ceil(pile / k) for pile in piles])
        return hour_need <= h