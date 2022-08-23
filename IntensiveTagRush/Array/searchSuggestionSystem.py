"""
1268. Search Suggestions System
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.
"""

import collections
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.suggestion = []

    def add_suggestion(self, product):
        if len(self.suggestion) < 3:
            self.suggestion.append(product)


class Solution:
    def suggestedProducts(self, products, searchWord):
        products = sorted(products)
        root = TrieNode()

        for p in products:
            node = root
            for char in p:
                node = node.children[char]
                node.add_suggestion(p)

        res, node = [], root
        for char in searchWord:
            node = node.children[char]
            res.append(node.suggestion)
        return res

# solution: Tire
# time: O(nlogn + n + s) where n = len(products) and s = len(searchWord
# space: O(n*m) where m = len(max length product)