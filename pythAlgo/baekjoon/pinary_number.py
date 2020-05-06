from sys import stdin
input = stdin.readline

N = int(input())
lst = [0 for _ in range(N)]
lst[0] = 1
lst[1] = 1
lst[2] = 2

for i in range(3, N):
    lst[i] = lst[i-1] + lst[i-2]

print(lst[N-1])