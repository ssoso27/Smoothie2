from sys import stdin
from collections import deque
input = stdin.readline

dd = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(i, j):
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()
        for dx, dy in dd:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and visitable[nx][ny]:
                q.append((nx, ny))
                visitable[nx][ny] = False

N = int(input())
town = []
for i in range(N):
    town.append(list(map(int, input().split(" "))))

max_cnt = 0
# 강우량이 0~100 일 때의 안전 영역의 최대 갯수 구하기
for water_level in range(101):
    # 지나갈 곳과 안지나갈 곳을 구분하기
    visitable = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # 잠기지 않는 곳은 지나갈 수 있음
            if town[i][j] > water_level:
                visitable[i][j] = True

    # 각 강우량 별 안전 영역 개수 구하기
    cnt = 0
    for i in range(N):
        for j in range(N):
            # 지나갈 수 있는 곳을 start로, bfs 돌리기
            if visitable[i][j]:
                visitable[i][j] = False
                bfs(i, j)
                cnt += 1

    # 최대 개수 구하기
    max_cnt = max(cnt, max_cnt)

print(max_cnt)