from sys import stdin
input = stdin.readline


def backtracking(cnt, last):
    if cnt == M:
        print(str.join(' ', arr))
        return

    for i in range(last, N):
        arr.append(str(lst[i]))
        backtracking(cnt+1, i)
        arr.pop()


N, M = map(int, input().split(" "))
lst = sorted(list(map(int, input().split(' '))))
arr = []
backtracking(0, 0)