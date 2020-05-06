from sys import stdin
input = stdin.readline

N, K = map(int, input().split(" "))
lst = list(map(int, input().split(" ")))

root = 0
for i in range(len(lst)):
    if lst[root] > lst[i]:
        root = i

min_value = float("inf")
for i in range(K-1):
    cnt = 0
    depth = len(lst[: root-i]), len(lst[root+1-i :])
    for d in depth:
        if d % (K-1) == 0:
            cnt += d // (K-1)
        else:
            cnt += (d // (K-1)) + 1
    min_value = min(min_value, cnt)
print(min_value)