def find_least_node(costs, checked):
    least_cost = float("inf")
    least_node = None

    for node in costs.keys():
        cost = costs[node]
        if not checked[node] and cost < least_cost:
            least_cost = cost
            least_node = node

    return least_node

def find_dijkstra_first_node(graph, start, end):
    checked = [False] * (len(graph))
    parents = {}
    costs = {}

    checked[start] = True
    parents[start] = None
    costs[start] = 0
    for node in graph[start].keys():
        parents[node] = start
        costs[node] = graph[start][node]

    neighbors = graph[start]
    current = find_least_node(costs, checked)
    while current is not None:
        neighbors.pop(current)
        checked[current] = True

        # 이웃 정점 가격 갱신
        neighbors.update(graph[current])
        print(neighbors)
        for neighbor in neighbors.keys():
            if neighbor not in costs.keys():
                costs[neighbor] = float("inf")
            new_cost = costs[current] + neighbors[neighbor]

            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = current

        current = find_least_node(costs, checked)

    # 첫번째 정점 찾기
    node = parents[end]
    while parents[node] != start:
        node = parents[node]
    return node


n, m = map(int, input().split(" "))
graph = {}

# 그래프 그려놓기
for i in range(n):
    graph[i] = {}
for _ in range(m):
    a, b, weight = map(int, input().split(" "))
    graph[a-1][b-1] = weight

# 경로표 그리기
path_table = [[-1] * n for _ in range(n)]
for a in range(n):
    for b in range(n):
        # node a -> b 까지 가는 최단경로 찾기
        if a == b:
            path_table[a][b] = "-"
            continue

        first_node = find_dijkstra_first_node(graph, a, b)
        path_table[a][b] = first_node

