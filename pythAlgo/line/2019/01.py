from sys import stdin
from collections import deque

input = stdin.readline


def backtracking(time, speed, cony, brown):
    print(time, speed, cony, brown)
    # 브라운이 범위를 벗어났을 때
    if brown < 0 or brown > 200000:
        return float("inf")
    # 코니가 너무 멀리 갔을 때
    if cony < 0 or cony > 200000:
        return time
    # 잡혔을때
    if cony == brown:
        return time

    speed = speed + 1
    cony = cony + speed

    return min(backtracking(time + 1, speed, cony, brown - 1),
               backtracking(time + 1, speed, cony, brown + 1),
               backtracking(time + 1, speed, cony, brown * 2))


def where_is_cony(c, t):
    print(c, t,  c + ((t*t + t) // 2))
    return c + ((t*t + t) // 2)


def bfs(brown):
    q = deque()
    q.append((brown, 0))

    while q:
        b, t = q.popleft()

        # 종료 조건 판별
        cony = where_is_cony(C, t)
        if (b == cony) or not (0 <= cony <= 200000):
            return t

        # 큐 채우기
        for i in range(3):
            bb = b
            if i == 0:
                bb = b - 1
            elif i == 1:
                bb = b + 1
            elif i == 2:
                bb = b * 2

            if not (0 <= bb <= 200000):
                continue

            q.append((bb, t + 1))


def bfs2():
    pass


C, B = map(int, input().split(" "))
# print(backtracking(0, 0, C, B))
# print(bfs(B))
print(bfs2())
