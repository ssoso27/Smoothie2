from sys import stdin
from collections import deque
input = stdin.readline

N, K = map(int, input().split(" "))

visited = [False for _ in range(100001)]
q = deque()
q.append((N, 0))
while q:
    position, time = q.popleft()
    visited[position] = True
    if position == K:
        print(time)
        break

    for p in (position-1, position+1, position*2):
        if 0 <= p <= 100000 and not visited[p]:
            q.append((p, time + 1))

