from sys import stdin
input = stdin.readline


def backtracking(cnt):
    if cnt == M:
        print(str.join(' ', arr))
        return

    for i in range(1, N+1):
        arr.append(str(i))
        backtracking(cnt+1)
        arr.pop()


N, M = map(int, input().split(" "))
arr = []
backtracking(0)