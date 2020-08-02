from sys import stdin
from collections import deque
input = stdin.readline
INF = float("inf")
dd = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs_fire(i, j):
    q = deque()
    q.append((0, i, j))

    while q:
        time, x, y = q.popleft()

        for dx, dy in dd:
            nx, ny = x + dx, y + dy
            # 유효한 좌표고 불이 더 빨리 도달할 수 있으면
            if 0 <= nx < h and 0 <= ny < w and copy[nx][ny] > time+1:
                copy[nx][ny] = time+1
                q.append((time+1, nx, ny))


def bfs_sangoon(i, j):
    q = deque()
    q.append((0, i, j))

    while q:
        time, x, y = q.popleft()

        for dx, dy in dd:
            nx, ny = x + dx, y + dy
            # 유효한 좌표고 불이 붙기 전에 도달할 수 있으면
            if 0 <= nx < h and 0 <= ny < w and copy[nx][ny] > time+1:
                # 만약 끝까지 도달했으면
                if nx == 0 or nx == h-1 or ny == 0 or ny == w-1:
                    return time+2

                q.append((time+1, nx, ny))
                copy[nx][ny] = 0 # 다시 방문하지 않도록 처리

    return "IMPOSSIBLE"



T = int(input())
for t in range(T):
    w, h = map(int, input().split(" "))
    building = []
    for i in range(h):
        building.append(input().rstrip("\n"))

    # 상근, 벽, 불의 위치들을 잡기
    start = (-1, -1)
    copy = [[INF] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if building[i][j] == "@":
                start = (i, j)
            elif building[i][j] == "#":
                copy[i][j] = -1
            elif building[i][j] == "*":
                copy[i][j] = 0

    # 불 bfs
    for i in range(h):
        for j in range(w):
            if copy[i][j] == 0:
                bfs_fire(i, j)

    # print(copy)

    # 상근 bfs
    print(bfs_sangoon(start[0], start[1]))


