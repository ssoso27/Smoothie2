from sys import stdin
input = stdin.readline

N, M, K = map(int, input().split(" "))
stickers = [[] for _ in range(K)]

for i in range(K):
    R, C = map(int, input().split(" "))
    for r in range(R):
        stickers[i].append(list(map(int, input().split(" "))))

print(stickers)