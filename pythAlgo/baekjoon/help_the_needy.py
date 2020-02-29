def find_least_node(costs, checked):
    least_cost = float("inf")
    least_node = None

    for node in costs.keys():
        cost = costs[node]
        if not checked[node] and cost < least_cost:
            least_cost = cost
            least_node = node

    return least_node

def get_length_by_dijkstra(graph, start):
    checked = [False] * len(graph)
    parents = {}
    costs = {}

    checked[start] = True
    parents[start] = None
    costs[start] = 0

    current = start
    while current is not None:
        checked[current] = True

        cost = costs[current]
        neighbors = graph[current]
        for neighbor in neighbors.keys():
            if neighbor not in costs.keys():
                costs[neighbor] = float("inf")

            new_cost = neighbors[neighbor] + cost
            if new_cost < costs[neighbor] and neighbor != current:
                costs[neighbor] = new_cost
                parents[neighbor] = current

        current = find_least_node(costs, checked)

    return max(costs.values())


N = int(input())
line_total = 0
graph = {}
for i in range(N):
    graph[i] = {}

for i in range(N):
    row = input()
    for j in range(len(row)):
        distance = 0
        if ord('A') <= ord(row[j]) <= ord('Z'):
            distance = ord(row[j]) - ord('A') + 27
        else:
            distance = ord(row[j]) - ord('a') + 1
        graph[i][j] = distance
        line_total += distance

min_length = float("inf")

for i in range(N):
    length = get_length_by_dijkstra(graph, i)
    print(length)
    if length < min_length:
        min_length = length

print(line_total - min_length)
