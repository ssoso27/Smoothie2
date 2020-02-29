def find_cheapest_node(costs, checked):
    cheapest_node = None
    cheapest_cost = float("inf")

    for node in costs.keys():
        if not checked[node] and costs[node] < cheapest_cost:
            cheapest_cost = costs[node]
            cheapest_node = node

    return cheapest_node


def make_dijkstra_parents(graph, start):
    checked = [False] * n
    parents = {}
    costs = {}

    checked[start] = True
    parents[start] = None
    costs[start] = 0
    for node in graph[start].keys():
        parents[node] = start
        costs[node] = graph[start][node]

    current = start
    while current is not None:
        checked[current] = True

        cost = costs[current]
        neighbors = graph[current]

        # 이웃 cost 갱신
        for neighbor in neighbors:
            if neighbor not in costs.keys():
                costs[neighbor] = float("inf")

            new_cost = cost + neighbors[neighbor]
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = current

        current = find_cheapest_node(costs, checked)
    return parents


def get_first_node(parents, start, end):
    node = end
    while parents[node] != start:
        node = parents[node]
    return node


n, m = map(int, input().split(" "))

graph = {}
for i in range(n):
    graph[i] = {}

for _ in range(m):
    a, b, weight = map(int, input().split(" "))
    graph[a-1][b-1] = weight
    graph[b-1][a-1] = weight

path_table = [[-1] * n for _ in range(n)]

for a in range(n):
    parents = make_dijkstra_parents(graph, a)
    for b in range(n):
        if a == b:
            path_table[a][b] = "-"
            continue

        first_node = get_first_node(parents, a, b)
        path_table[a][b] = first_node + 1

for row in path_table:
    print(" ".join(map(str, row)))

