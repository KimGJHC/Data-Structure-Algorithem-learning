"""
2115. Find All Possible Recipes from Given Supplies
You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. Ingredients to a recipe may need to be created from other recipes, i.e., ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.
"""

import collections
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = collections.defaultdict(int)
        graph = collections.defaultdict(list)
        for rec, ing in zip(recipes, ingredients):
            indegree[rec] = len(ing)
            for i in ing:
                graph[i].append(rec)

        res = []
        queue = collections.deque(supplies)
        recipes = set(recipes)

        while queue:
            x = queue.popleft()
            if x in recipes:
                res.append(x)
            for xx in graph[x]:
                indegree[xx] -= 1
                if indegree[xx] == 0:
                    queue.append(xx)
        return res
# solution 1: topological sorting
# time: O(n + max(len of ingredients))
# space: O(n)