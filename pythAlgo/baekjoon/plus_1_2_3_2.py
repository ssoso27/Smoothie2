from sys import stdin
input = stdin.readline


def backtracking(total, lst):
    if total == n:
        results.append('+'.join(lst))
        return

    for i in [1, 2, 3]:
        if total+i <= n:
            lst.append(str(i))
            backtracking(total+i, lst)
            lst.pop()


n, k = map(int, input().split())
results = []
backtracking(0, [])

if len(results) >= k:
    print(results[k-1])
else:
    print(-1)