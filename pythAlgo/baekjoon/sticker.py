from sys import stdin
input = stdin.readline

N = int(input())
lst = list(map(int, input().split()))

up = [1 for _ in range(N)]
down = [1 for _ in range(N)]

last = lst[0]
for i in range(1, N):
    if lst[i] >= last:
        up[i] = up[i-1] + 1

    if lst[i] <= last:
        down[i] = down[i-1] + 1

    last = lst[i]

print(max(max(up), max(down)))