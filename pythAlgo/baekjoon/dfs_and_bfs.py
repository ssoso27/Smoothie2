from collections import deque
from sys import stdin
input = stdin.readline


def dfs(start):
    visited = [False for _ in range(N+1)]
    stack = [start]

    path = ''
    while stack:
        v = stack.pop()

        if visited[v]:
            continue

        visited[v] = True
        path += ' ' + str(v)
        for next in sorted(graph[v], reverse=True):
            if not visited[next]:
                stack.append(next)

    print(path.strip())

def bfs(start):
    visited = [False for _ in range(N+1)]
    q = deque()
    q.append(start)
    visited[start] = True

    path = ''
    while q:
        v = q.popleft()
        path += ' ' + str(v)
        for next in sorted(graph[v]):
            if not visited[next]:
                q.append(next)
                visited[next] = True

    print(path.strip())


N, M, V = map(int, input().split())
graph = {}
for i in range(1, N+1):
    graph[i] = []

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(V)
bfs(V)