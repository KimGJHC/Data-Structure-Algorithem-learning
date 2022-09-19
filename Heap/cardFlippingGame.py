"""
822. Card Flipping Game
You are given two 0-indexed integer arrays fronts and backs of length n, where the ith card has the positive integer fronts[i] printed on the front and backs[i] printed on the back. Initially, each card is placed on a table such that the front number is facing up and the other is facing down. You may flip over any number of cards (possibly zero).

After flipping the cards, an integer is considered good if it is facing down on some card and not facing up on any card.

Return the minimum possible good integer after flipping the cards. If there are no good integers, return 0.
"""

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        impossible = set()
        visited = set()

        for f, b in zip(fronts, backs):
            if f == b:
                impossible.add(f)
            else:
                visited.add(f)
                visited.add(b)

        cards = list(visited)
        heapq.heapify(cards)

        while cards:
            small_card = heapq.heappop(cards)
            if small_card not in impossible:
                return small_card

        return 0