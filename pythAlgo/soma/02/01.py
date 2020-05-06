from sys import stdin
input = stdin.readline

N = int(input())
sugar_contents = list(map(int, input().split(" ")))

bigger = [0 for _ in range(N)]
bigger[0] = sugar_contents[0]
max_sugar = sugar_contents[0]

for i in range(1, N):
    bigger[i] = max(sugar_contents[i], bigger[i-1] + sugar_contents[i])
    max_sugar = max(max_sugar, bigger[i])

print(max_sugar)