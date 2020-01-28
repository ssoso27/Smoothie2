from collections import deque


def move_knight2():
    l = int(input())
    sx, sy = map(int, input().split(" "))
    ex, ey = map(int, input().split(" "))

    dx = [-2, -1, +1, +2, -2, -1, +2, +1]
    dy = [-1, -2, -2, -1, +1, +2, +1, +2]

    levels = [[0]*l for _ in range(l)]
    queue = deque()
    queue.append((sx, sy))

    while queue:
        tx, ty = queue.popleft()

        if tx == ex and ty == ey:
            return levels[tx][ty]

        for i in range(8):
            x = tx + dx[i]
            y = ty + dy[i]
            if x < 0 or x >= l or y < 0 or y >= l:
                continue
            if not levels[x][y]:
                levels[x][y] = levels[tx][ty]+1
                queue.append((x, y))


len_case = int(input())
for i in range(len_case):
    print(move_knight2())
