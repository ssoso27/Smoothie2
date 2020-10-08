from collections import deque
from sys import stdin
input = stdin.readline


def bfs(starts, cnt_zero, checked):
    if cnt_zero == 0:
        return 0

    q = deque()
    q.extend(starts)

    while q:
        h, n, m, day = q.popleft()

        for dh, dn, dm in dd:
            nh, nn, nm = h + dh, n + dn, m + dm

            if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M:
                if checked[nh][nn][nm]:
                    continue

                cnt_zero -= 1
                if cnt_zero == 0: # 다 익었으면
                    return day+1

                q.append((nh, nn, nm, day+1))
                checked[nh][nn][nm] = True

    return -1


M, N, H = map(int, input().split())

cnt_zero = 0
starts = []
checked = [[[True for _ in range(M)] for _ in range(N)] for _ in range(H)]
dd = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

box3d = []
for h in range(H):
    box2d = []
    for n in range(N):
        row = list(map(int, input().split()))
        box2d.append(row)
        for r in range(len(row)):
            if row[r] == 0:
                cnt_zero += 1
                checked[h][n][r] = False
            elif row[r] == 1:
                starts.append((h, n, r, 0))

    box3d.append(box2d)

print(bfs(starts, cnt_zero, checked))