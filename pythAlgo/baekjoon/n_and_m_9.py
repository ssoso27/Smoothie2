from sys import stdin
input = stdin.readline


def backtracking(cnt):
    if cnt == M:
        results.add(tuple(arr))
        return

    for i in range(N):
        if not checked[i]:
            arr.append(lst[i])
            checked[i] = True

            backtracking(cnt+1)

            arr.pop()
            checked[i] = False


N, M = map(int, input().split(" "))
lst = sorted(list(map(int, input().split(" "))))
arr = []
checked = [False for _ in range(N)]
results = set()
backtracking(0)

for r in sorted(list(results)):
    print(str.join(' ', map(str, r)))
