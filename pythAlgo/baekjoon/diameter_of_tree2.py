# 임의의 노드 A에서 가장 먼 노드 B는 반드시 이 트리의 지름을 구성하게 된다.
from collections import deque


def find_furthest_node(start):
    max_index = start
    max_value = 0

    queue = deque()
    queue.append(start)

    distances = [-1 for _ in range(n+1)]
    distances[start] = 0

    # bfs
    while queue:
        # 노드를 가져와서
        current = queue.popleft()
        # 그 이웃들을 찾고
        neghibors = graph[current]
        # 그 이웃들에 대하여
        for neghibor in neghibors.keys():
            # 방문한 적 없는 노드면
            if distances[neghibor] == -1:
                # 거리를 더하고
                distances[neghibor] = distances[current] + neghibors[neghibor]
                # 큐에 그 이웃을 추가
                queue.append(neghibor)
                # 최댓값인지 판별
                if max_value < distances[neghibor]:
                    max_index = neghibor
                    max_value = distances[neghibor]

    return (max_index, max_value)


n = int(input())
graph = {}
for i in range(1, n+1):
    graph[i] = {}

# 그래프 그리기
for _ in range(n-1):
    v, u, weight = map(int, input().split(" "))
    graph[v][u] = weight
    graph[u][v] = weight

# 노드 1에서 가장 먼 노드 B 찾기
v = find_furthest_node(1)
u = find_furthest_node(v[0])

print(u[1])