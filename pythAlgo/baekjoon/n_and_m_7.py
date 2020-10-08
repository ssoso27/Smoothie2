from sys import stdin
input = stdin.readline


def backtracking(cnt):
    if cnt == M:
        print(str.join(' ', arr))
        return

    for i in range(N):
        arr.append(lst[i])
        backtracking(cnt+1)
        arr.pop()


N, M = map(int, input().split(" "))
lst = sorted(input().strip().split(' '))
arr = []
backtracking(0)