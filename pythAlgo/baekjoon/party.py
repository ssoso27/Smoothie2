def find_nearest_node(costs, checked):
    nearest_node = None
    nearest_cost = float("inf")

    for node in costs.keys():
        cost = costs[node]
        if not checked[node] and cost < nearest_cost:
            nearest_cost = cost
            nearest_node = node

    return nearest_node


def dijkstra(start, end):
    # 지나간 node
    checked = [False] * (N+1)
    checked[start] = True

    # 소요시간 cost
    costs = {}
    costs[start] = 0

    # 초기화
    for node in graph[start].keys():
        costs[node] = graph[start][node]

    current = find_nearest_node(costs, checked)
    while current is not None:
        # 파티 장소인지 확인
        if current == end:
            # end 정보 빼고 리셋
            checked = [False] * (N+1)
            checked[current] = True
            costs = {
                end: costs[end]
            }

        # 집으로 돌아왔는지 확인
        if current == start:
            return costs[current]

        # 지나갔다고 체크
        checked[current] = True

        # 이웃들의 가격 조사
        neighbors = graph[current]
        for neighbor in neighbors.keys():
            if neighbor not in costs.keys():
                costs[neighbor] = float("inf")

            # 이웃 가격 갱신
            new_cost = costs[current] + neighbors[neighbor]
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
        current = find_nearest_node(costs, checked)


N, M, X = map(int, input().split(" "))
roads = [map(int, input().split(" ")) for _ in range(M)]

# 그래프화
graph = {}
for i in range(1, N+1):
    graph[i] = {}
for road in roads:
    v, u, t = road
    graph[v][u] = t

# 최대 시간 찾기
max_time = -1
for i in range(1, N+1):
    if i == X: # 자기네 마을에서 파티하는 애는 이동시간이 0이다.
        continue
    max_time = max(max_time, dijkstra(i, X))

print(max_time)