import heapq

class Dijkstra:
    def __init__(self, graph):
        self.graph = graph

    def run(self, start):
        dist = {v: float('inf') for v in self.graph}
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in self.graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        return dist
