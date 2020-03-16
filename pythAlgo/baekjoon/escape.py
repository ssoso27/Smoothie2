from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

R, C = map(int, input().split(" "))
# forest = [ [-1] * C for _ in range(R)]
forest = [input() for _ in range(R)]
overflow = [ [-1] * C for _ in range(R)]

queue = deque()
sx, sy = -1
ex, ey = -1

for i in range(R):
    for j in range(C):
        if forest[i][j] == '*':
            overflow[i][j] = 0
            queue.append((i, j))
        elif forest[i][j] == 'S':
            sx, sy = i, j
        elif forest[i][j] == 'D':
            ex, ey = i, j

# 범람 시기 알아내기
while queue:
    i, j = queue.popleft()
    level = overflow[i][j]
    for d in range(len(dx)):
        x = i + dx[d]
        y = j + dy[d]
        if 0 <= x < R and 0 <= y < C and forest[x][y] not in 'XD' and overflow[x][y] == -1:
            overflow[x][y] = level + 1
            queue.append((x, y))

# 고슴도치 이동시키기
dochi_level = [ [-1] * C for _ in range(R)]
dochi_level[sx][sy] = 0
queue = deque()
queue.append((sx, sy))
while queue:
    i, j = queue.popleft()
    level = dochi_level[i][j]
    for d in range(len(dx)):
        x = i + dx[d]
        y = j + dy[d]
        if 0 <= x < R and 0 <= y < C and forest[x][y] not in '*X':
            if dochi_level[x][y] == -1 and (overflow[x][y] == -1 or level + 1 < overflow[x][y]):
                queue.append((x, y))
                dochi_level[x][y] = level+1

if dochi_level[ex][ey] != -1:
    print(dochi_level[ex][ey])
else:
    print('KAKTUS')