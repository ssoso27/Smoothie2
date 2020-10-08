from collections import deque
from sys import stdin
input = stdin.readline


def bfs(start, end):
    checked = [False for _ in range(N+1)]
    q = deque()
    q.append((start, 0))
    checked[start] = True

    while q:
        node, level = q.popleft()

        for next in graph[node]:
            if not checked[next]:
                if next == end:
                    return level+1

                q.append((next, level+1))
                checked[next] = True

    return -1

N = int(input())
start, end = map(int, input().split())

graph = {}
for i in range(N+1):
    graph[i] = []

M = int(input())
for _ in range(M):
    v, u = map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)

print(bfs(start, end))
