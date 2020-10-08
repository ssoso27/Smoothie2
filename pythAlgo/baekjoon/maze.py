from collections import deque
from sys import stdin
input = stdin.readline


def bfs():
    checked = maze.copy() # 1이어야만 갈 수 있음
    q = deque()
    q.append((0, 0, 1)) # 시작 지점
    checked[0][0] = "0"

    while q:
        x, y, level = q.popleft()

        # 상하좌우 확인해보기
        for dx, dy in dd:
            nx, ny = dx + x, dy + y
            if 0 <= nx < N and 0 <= ny < M and checked[nx][ny] == "1":
                if nx == N-1 and ny == M-1:
                    return level+1

                q.append((nx, ny, level+1))
                checked[nx][ny] = "0"

N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(input().strip()))

dd = [(1, 0), (-1, 0), (0, 1), (0, -1)]

print(bfs())