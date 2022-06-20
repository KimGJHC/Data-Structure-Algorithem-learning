from heapq import *

class Solution:

    def alien_order(self, words):
        # Write your code here

        # get all the letter that should be included
        all_letters = set(list(''.join(words)))

        graph = {letter: [] for letter in all_letters}
        inDegree = {letter: 0 for letter in all_letters}

        # create graph
        for samller_idx in range(len(words)):
            for larger_idx in range(samller_idx + 1, len(words)):
                Ineq = self.getIneq(words[samller_idx], words[larger_idx])
                if Ineq == 'NoInfo':
                    continue
                elif not Ineq:
                    return ""
                else:
                    # add the edge
                    graph[Ineq[0]].append(Ineq[1])
                    inDegree[Ineq[1]] += 1

        # Get topological sort order
        order = ''
        TOTAL_EDGE = sum(len(next_word) for next_word in graph.values())
        removedEdge = 0
        heap = [letter for letter in graph if inDegree[letter] == 0]
        heapify(heap)

        while heap:
            current_letter = heappop(heap)
            order += current_letter
            for neighbor in graph[current_letter]:
                inDegree[neighbor] -= 1
                removedEdge += 1
                if inDegree[neighbor] == 0:
                    heappush(heap, neighbor)
        return order if removedEdge == TOTAL_EDGE else ''

    def getIneq(self, x, y):
        # we know x < y, return the letter in x that is smaller than the corresponding letter in your
        i = 0
        x_len, y_len = len(x), len(y)
        MAX = min(x_len, y_len)

        while i < MAX:
            if x[i] != y[i]:
                return (x[i], y[i])
            i += 1

        if y_len < x_len:
            return False
        else:
            return 'NoInfo'
