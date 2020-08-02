from sys import stdin
from collections import deque
input = stdin.readline

dd = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def safe_area(town, water_level):
    cnt = 0
    checked = [[False for _ in range(N)] for _ in range(N)]

    # for i in range(N):
    #     for j in range(N):
    #         if town[i][j] > water_level and not checked[i][j]:
    #             # bfs로 영역 체크
    #             cnt += 1
    #             q = deque()
    #             q.append((i, j))
    #
    #             while q:
    #                 x, y = q.popleft()
    #                 checked[x][y] = True
    #
    #                 for dx, dy in dd:
    #                     nx, ny = x+dx, y+dy
    #                     if 0 <= nx < N and 0 <= ny < N and town[nx][ny] > water_level and not checked[nx][ny]:
    #                         q.append((nx, ny))

    graph = {}
    for i in range(N):
        for j in range(N):
            if town[i][j] > water_level:
                # 이웃 노드 넣기
                graph[(i, j)] = []
                for dx, dy in dd:
                    nx, ny = i+dx, j+dy
                    if 0 <= nx < N and 0 <= ny < N and town[nx][ny] > water_level:
                        graph[(i, j)].append((nx, ny))

    # bfs 로 영역 찾기
    while graph:
        q = deque()
        start = list(graph.keys())[0]
        print(type(start))
        q.append(start)
        cnt += 1

        while q:
            x, y = q.popleft()
            checked[x][y] = True

            negibors = graph.pop(start)
            for nx, ny in negibors:
                if not checked[nx][ny]:
                    q.append((nx, ny))

    return cnt


N = int(input())
town = []
for i in range(N):
    town.append(list(map(int, input().split(" "))))

answer = 0
for i in range(1, 101):
    result = safe_area(town, i)
    if result == 0:
        break
    answer = max(answer, result)

print(answer)