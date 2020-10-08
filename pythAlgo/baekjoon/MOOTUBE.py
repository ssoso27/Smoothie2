from sys import stdin
input = stdin.readline

N, Q = map(int, input().split(" "))

graph = {}
for i in range(N):
    graph[N] = {}

for _ in range(N-1):
    p, q, r = map(int, input().split(" "))
    graph[p][q] = r
    graph[q][p] = r

for _ in range(Q):
    k, v = map(int, input().split(" "))
    # K=k 라면, 동영상 v를 보고 있는 소들에게 몇 개의 동영상이 추천될까?

    