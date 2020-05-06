from sys import stdin
from _collections import deque
input = stdin.readline

MIN = 1
MAX = 100000000

N, M = map(int, input().split(" "))

x_array = [0 for _ in range(N)]
y_array = [0 for _ in range(N)]
for i in range(N):
    x_array[i], y_array[i] = map(int, input().split(" "))

relations = []
for i in range(M):
    # relations[i] = [i-1 for i in (map(int, input().split(" ")))]
    u, v = map(int, input().split(" "))
    if u == v:
        continue
    relations.append((u-1, v-1))

# bfs로 각 팀을 찾고, 그 팀의 최소최대 xy 구하기
# 그래프 그리기
graph = {}
for i in range(N):
    graph[i] = []
for i in range(len(relations)):
    u, v = relations[i]
    graph[u].append(v)
    graph[v].append(u)

# bfs
remain = [i for i in range(N)]
answer = 0

while remain:
    max_x, max_y, min_x, min_y = MIN-1, MIN-1, MAX+1, MAX+1

    q = deque()
    q.append(remain.pop())
    while q:
        top = q.popleft()

        # x, y 판별
        min_x = min(min_x, x_array[top])
        max_x = max(max_x, x_array[top])
        min_y = min(min_y, y_array[top])
        max_y = max(max_y, y_array[top])

        # 큐에 넣기
        for next in graph[top]:
            if next in remain:
                q.append(next)
                remain.remove(next)

    # 해당 팀의 둘레 판별
    result = (max_x - min_x)*2 + (max_y - min_y)*2
    answer = max(answer, result)

print(answer)


