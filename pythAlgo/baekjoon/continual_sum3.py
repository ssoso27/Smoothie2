from sys import stdin
input = stdin.readline

n = int(input())
lst = list(map(int, input().split(" ")))

bigger = [0 for _ in range(n)]
bigger[0] = lst[0]
answer = lst[0]
for i in range(1, n):
    bigger[i] = max(lst[i], bigger[i-1] + lst[i])
    answer = max(answer, bigger[i])

print(answer)
