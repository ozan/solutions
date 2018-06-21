"""
How long will it take for a message to propagate from K to all nodes on a network?

Strategy: apply Dijkstra's for the shortest path from K to all other nodes, then
return the largest result. If a node cannot be reached, return -1.
"""

from collections import defaultdict
import heapq


class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        queue = [(0, K)]
        distances = defaultdict(lambda: 0)
        while queue:
            cost, u = heapq.heappop(queue)
            if u in distances:
                continue
            distances[u] = cost
            for v, w in graph[u]:
                heapq.heappush(queue, (cost+w, v))

        if len(distances) < N: return -1
        return max(distances.values())
        
