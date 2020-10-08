from sys import stdin
input = stdin.readline


def backtracking(cnt, last):
    if cnt == M:
        results.add(tuple(arr))
        return

    for i in range(last, N):
        arr.append(lst[i])
        backtracking(cnt+1, i)
        arr.pop()


N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))

arr = []
results = set()

backtracking(0, 0)

for r in sorted(results):
    print(str.join(' ', map(str, r)))