from sys import stdin
input = stdin.readline

N = int(input())
counts = [0 for _ in range(N+1)]

for i in range(2, N+1):
    counts[i] = counts[i-1] + 1

    if i % 3 == 0 and counts[i//3] < counts[i]:
        counts[i] = counts[i//3] + 1

    if i % 2 == 0 and counts[i//2] < counts[i]:
        counts[i] = counts[i//2] + 1

print(counts[N])