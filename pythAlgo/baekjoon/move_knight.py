from collections import deque


def move_knight():
    l = int(input())
    sx, sy = map(int, input().split(" "))
    ex, ey = map(int, input().split(" "))

    if (sx, sy) == (ex, ey):
        return 0

    dx = [-2, -1, +1, +2, -2, -1, +2, +1]
    dy = [-1, -2, -2, -1, +1, +2, +1, +2]

    checked = [(sx, sy)]
    queue = deque()

    for i in range(8):
        x = sx + dx[i]
        y = sy + dy[i]
        if 0 <= x < l and 0 <= y < l:
            queue.append((1, x, y))

    while queue:
        level, tx, ty = queue.popleft()
        if (tx, ty) not in checked:
            checked.append((tx, ty))
            if (tx, ty) == (ex, ey):
                return level

            for i in range(8):
                x = tx + dx[i]
                y = ty + dy[i]
                if (x, y) not in checked and 0 <= x < l and 0 <= y < l:
                    queue.append((level + 1, x, y))


len_case = int(input())
for i in range(len_case):
    print(move_knight())
