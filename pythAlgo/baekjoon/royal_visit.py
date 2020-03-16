from sys import stdin
input = stdin.readline

N, M = map(int, input().split(" "))
A, B, K, G = map(int, input().split(" "))
godoolra_path = list(map(int, input().split(" ")))
roads = {}
for i in range(1, N+1):
    roads[i] = {}

for _ in range(M):
    U, V, L = map(int, input().split(" "))
    roads[U][V] = L

print(roads)

# 금지시간 구하기
time = 0
ban_times = {}
for i in range(1, N+1):
    ban_times[i] = {}

for i in range(1, G):
    u, v = godoolra_path[i-1], godoolra_path[i]
    end_time = time + roads[u][v] - 1
    ban_times[u][v] = (time, end_time)
    time = end_time

print(ban_times)