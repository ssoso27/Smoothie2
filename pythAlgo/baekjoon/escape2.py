from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(type, starts):
    queue = deque()
    queue.extend(starts)

    while queue:
        cx, cy = queue.popleft()
        for d in range(len(dx)):
            nx = dx[d] + cx
            ny = dy[d] + cy
            if 0 <= nx < R and 0 <= ny < C:
                if type == 'w':
                    # 물이 차는 시간 채우기
                    if forest[nx][ny] not in 'XD' and water_time[nx][ny] == -1:
                        water_time[nx][ny] = water_time[cx][cy] + 1
                        queue.append((nx, ny))

                elif type == 'd':
                    # 도치가 이동하는 시간 채우기
                    if forest[nx][ny] == 'D': # 도달한 경우
                        dochi_time[nx][ny] = dochi_time[cx][cy] + 1
                        return

                    if forest[nx][ny] == '.' and dochi_time[nx][ny] == -1 and \
                            (dochi_time[cx][cy] + 1 < water_time[nx][ny] or water_time[nx][ny] == -1):
                        dochi_time[nx][ny] = dochi_time[cx][cy] + 1
                        queue.append((nx, ny))


R, C = map(int, input().split(" "))
forest = [input() for _ in range(R)]
sx, sy = -1, -1
ex, ey = -1, -1
waters = []

water_time = [[-1]*C for _ in range(R)]
dochi_time = [[-1]*C for _ in range(R)]

# 초기화
for r in range(R):
    for c in range(C):
        if forest[r][c] == '*':
            waters.append((r, c))
            water_time[r][c] = 0
        elif forest[r][c] == 'S':
            sx, sy = r, c
            dochi_time[sx][sy] = 0
        elif forest[r][c] == 'D':
            ex, ey = r, c

bfs('w', waters)
bfs('d', [(sx, sy)])

if dochi_time[ex][ey] == -1:
    print('KAKTUS')
else:
    print(dochi_time[ex][ey])