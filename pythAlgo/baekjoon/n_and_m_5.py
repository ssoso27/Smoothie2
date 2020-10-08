from sys import stdin
input = stdin.readline


def backtracking(cnt):
    if cnt == M:
        print(str.join(' ', arr))
        return

    for i in range(0, N):
        if not checked[i]:
            arr.append(str(lst[i]))
            checked[i] = True

            backtracking(cnt+1)

            arr.pop()
            checked[i] = False


N, M = map(int, input().split(" "))
lst = sorted(list(map(int, input().split(" "))))
arr = []
checked = [False for _ in range(N)]
backtracking(0)