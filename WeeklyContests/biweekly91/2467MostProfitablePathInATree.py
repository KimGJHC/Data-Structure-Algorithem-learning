"""
2467. Most Profitable Path in a Tree
There is an undirected tree with n nodes labeled from 0 to n - 1, rooted at node 0. You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

At every node i, there is a gate. You are also given an array of even integers amount, where amount[i] represents:

the price needed to open the gate at node i, if amount[i] is negative, or,
the cash reward obtained on opening the gate at node i, otherwise.
The game goes on as follows:

Initially, Alice is at node 0 and Bob is at node bob.
At every second, Alice and Bob each move to an adjacent node. Alice moves towards some leaf node, while Bob moves towards node 0.
For every node along their path, Alice and Bob either spend money to open the gate at that node, or accept the reward. Note that:
If the gate is already open, no price will be required, nor will there be any cash reward.
If Alice and Bob reach the node simultaneously, they share the price/reward for opening the gate there. In other words, if the price to open the gate is c, then both Alice and Bob pay c / 2 each. Similarly, if the reward at the gate is c, both of them receive c / 2 each.
If Alice reaches a leaf node, she stops moving. Similarly, if Bob reaches node 0, he stops moving. Note that these events are independent of each other.
Return the maximum net income Alice can have if she travels towards the optimal leaf node.

# The key is to figure out the path from bob to root, with which we can decide the nodes with which we modify amounts
# use bfs to find path and use dfs to get maxmized reward
"""


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        self.adjList = defaultdict(list)
        for start, end in edges:
            self.adjList[start].append(end)
            self.adjList[end].append(start)

        # bfs
        queue = deque([(bob, None, [])])

        while queue:
            node, prev, path = queue.popleft()
            path.append(node)
            if node == 0:
                break
            else:
                for neighbor in self.adjList[node]:
                    if neighbor != prev:
                        queue.append((neighbor, node, path[:]))
        print(path)

        # we will know the path between B to root now
        path_length = len(path)
        for i in range(path_length // 2):
            amount[path[i]] = 0
        if path_length % 2 == 1:
            amount[path[path_length // 2]] //= 2
        print(amount)

        # use dfs to compute reward
        def dfs(node, prev):
            # return max reward from node to leaves
            if prev != None and len(self.adjList[node]) == 1:
                return amount[node]

            max_R = float('-inf')
            for neighbor in self.adjList[node]:
                if neighbor == prev:
                    continue
                else:
                    max_R = max(max_R, dfs(neighbor, node))
            max_R += amount[node]
            return max_R

        res = dfs(0, None)
        return res


