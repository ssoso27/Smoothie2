from collections import deque
from sys import stdin
input = stdin.readline


def bfs():
    checked = [False for _ in range(N+1)]
    q = deque()
    q.append(1)
    checked[1] = True

    cnt = -1
    while q:
        node = q.popleft()
        cnt += 1

        for next in graph[node]:
            if not checked[next]:
                q.append(next)
                checked[next] = True

    return cnt

N = int(input())
M = int(input())

graph = {}
for i in range(N+1):
    graph[i] = []

for _ in range(M):
    v, u = map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)

print(bfs())