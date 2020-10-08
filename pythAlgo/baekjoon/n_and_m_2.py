from sys import stdin
input = stdin.readline


def backtracking(cnt, last):
    if cnt == M:
        print(str.join(' ', arr))
        return

    for i in range(last+1, N+1):
        if not checked[i]:
            arr.append(str(i))
            checked[i] = True
            backtracking(cnt+1, i)

            arr.pop()
            checked[i] = False


N, M = map(int, input().split(" "))
arr = []
checked = [False for _ in range(N+1)]
backtracking(0, 0)