from sys import stdin
input = stdin.readline


def get_next(x, y):
    if y == M-1:
        return x+1, 0
    return x, y+1


def get_prev(x, y):
    if y == 0:
        return x-1, M-1
    return x, y-1


N, M = map(int, input().split(" "))

arr = [[0]*M for _ in range(N)]
sum_arr = [[0]*M for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split(" ")))
    for j in range(M):
        if i == 0 and j == 0:
            sum_arr[i][j] = arr[i][j]
            continue

        prev_coord = get_prev(i, j)
        sum_arr[i][j] = sum_arr[prev_coord[0]][prev_coord[1]] + arr[i][j]

K = int(input())
for _ in range(K):
    # (i, j) ~ (x, y) 닫힌 구간의 합
    i, j, x, y = [d-1 for d in map(int, input().split(" "))]
    if i == 0 and j == 0:
        print(sum_arr[x][y])
    elif i == x and j == y :
        print(arr[i][j])
    else:
        result = (sum_arr[x][y] - sum_arr[x][get_prev(x, j)[1]]) + (sum_arr[i][y] - sum_arr[i][get_prev(i, j)[1]])
        print(result)


