import heapq
from sys import stdin
input = stdin.readline
INF = float("inf")


def dijkstra(start, end):
    dist = [INF for _ in range(N+1)]
    dist[start] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q:
        time, village = heapq.heappop(q)

        for ntime, nviliage in graph[village]:
            ntime += time
            if dist[nviliage] > ntime:
                dist[nviliage] = ntime
                heapq.heappush(q, (ntime, nviliage))

    return dist

N, M, X = map(int, input().split(" "))
graph = [[] for _ in range(N+1)]
for i in range(M):
    v, u, t = map(int, input().split(" "))
    graph[v].append((t, u))

# 파티 장소로 가기
max_time = -1
transfer_times = [[0] for _ in range(N+1)]
for i in range(1, N+1):
    if i == X:
        continue
    transfer_times[i] = dijkstra(i, X)[X]

comeback_times = dijkstra(X, None)
# 집으로 돌아가기
for i in range(1, N+1):
    if i == X:
        continue
    transfer_times[i] += comeback_times[i]
    max_time = max(transfer_times[i], max_time)

print(max_time)