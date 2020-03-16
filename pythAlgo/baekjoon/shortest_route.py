import heapq
from sys import stdin
input = stdin.readline

def dijkstra(start):
    dist = [INF for _ in range(V+1)]
    dist[start] = 0

    q = []
    heapq.heappush(q, [0, start])

    while q:
        weight, node = heapq.heappop(q)

        # 이웃 노드들 조사
        for nw, nn in graph[node]:
            nw += weight
            if nw < dist[nn]:
                dist[nn] = nw
                heapq.heappush(q, [nw, nn])

    return dist

INF = float("inf")
V, E = map(int, input().split(" "))
K = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split(" "))
    graph[u].append([w, v])

for dist in dijkstra(K)[1:]:
    if dist == INF:
        print("INF")
    else:
        print(dist)
