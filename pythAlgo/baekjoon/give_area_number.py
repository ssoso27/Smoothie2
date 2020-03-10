from collections import deque

N = int(input())
visited = [[False]*N for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(start): # 이어진 모든 집 찾기
    count = 1
    visited[start[0]][start[1]] = True

    queue = deque()
    queue.append(start)

    while queue:
        current = queue.popleft()
        for d in range(len(dx)): # current 기준 모든 방향에 대해서
            x = current[0] + dx[d]
            y = current[1] + dy[d]
            if 0 <= x < N and 0 <= y < N and not visited[x][y] and matrix[x][y] == '1':
                # 단지에 집 하나 추가
                count += 1
                visited[x][y] = True
                queue.append( (x, y) )

    return count

houses_in_area = []
matrix = []
for _ in range(N):
    matrix.append(input())

for i in range(N):
    for j in range(N):
        if not visited[i][j] and matrix[i][j] == '1':
            houses_in_area.append(bfs((i, j)))

houses_in_area.sort()
print(len(houses_in_area))
for h in houses_in_area:
    print(h)