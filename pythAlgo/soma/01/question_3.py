from sys import stdin
input = stdin.readline

N, K = map(int, input().split(" "))
origin = list(map(int, input().split(" ")))

# origin의 갭 구하기
gaps = [-1] * (N-1)
for i in range(0, N-1):
    gaps[i] = (i, i+1, origin[i+1]-origin[i])

# 가장 큰 갭 K-1개 빼기
gaps.sort(key = lambda gap: gap[2])
for _  in range(K-1):
    gaps.pop()

# 갭 합 더하기
total = 0
for gap in gaps:
    total += gap[2]

print(total)