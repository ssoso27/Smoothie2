from sys import stdin
from collections import deque
input = stdin.readline
INF = float("inf")


# start -> 모든 노드에 대한 케빈 베이컨 수를 구하는 함수
def kebin_bacon(graph, start):
    kebin = [INF] * (len(graph)+1)

    q = deque()
    q.append((0, start))

    while q:
        level, node = q.popleft()
        if kebin[node] != INF: # 이미 방문한 노드
            continue

        kebin[node] = level

        # 이웃 노드 넣기
        for neighbor in graph[node]:
            q.append((level+1, neighbor))

    return sum(kebin[1:])


N, M = map(int, input().split(" "))

graph = {}
for i in range(1, N+1):
    graph[i] = []

for i in range(M):
    A, B = map(int, input().split(" "))
    graph[A].append(B)
    graph[B].append(A)

min_kebin = 0
min_kebin_value = INF
for i in range(1, N+1):
    result = kebin_bacon(graph, i)
    if result < min_kebin_value:
        min_kebin, min_kebin_value = i, result

print(min_kebin)