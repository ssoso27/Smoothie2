from sys import stdin
input = stdin.readline

dx = [0, 1, 0, 1]
dy = [0, 0, 1, 1]

T = int(input())
while T > 0:
    N, M = map(int, input().split(" "))
    drawing = [[] for _ in range(N)]
    painted = [[0]*M for _ in range(N)]

    for i in range(N):
        drawing[i] = list(map(int, input().split(" ")))

    for r in range(N-1):
        for c in range(M-1):
            if drawing[r][c] == 1:
                for d in range(len(dx)):
                    nx = r + dx[d]
                    ny = c + dy[d]

                    if not (0 <= nx < N and 0 <= ny < M and drawing[nx][ny] == 1):
                        break

                    painted[nx][ny] = 1

    if drawing == painted:
        print("YES")
    else:
        print("NO")

    T -= 1