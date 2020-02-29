def find_cheapest_node(costs, checked):
    min_cost = float("inf")
    min_node = None

    for node in costs.keys():
        cost = costs[node]
        if not checked[node] and min_cost > cost:
            min_cost = cost
            min_node = node

    return min_node

def get_max(dict):
    max = -1
    for k in dict.keys():
        v = dict[k]
        if v > max:
            max = v
    return max

def hacking():
    graph = {}

    n, d, c = map(int, input().split(" "))
    for i in range(n):
        graph[i] = {}

    for _ in range(d):
        a, b, s = map(int, input().split(" "))
        graph[b-1][a-1] = s

    checked = [False] * n
    costs = {}
    parents = {}

    start = c-1
    checked[start] = True
    costs[start] = 0
    parents[start] = None
    for node in graph[start]:
        costs[node] = graph[start][node]
        parents[node] = start

    current = find_cheapest_node(costs, checked)
    while current is not None:
        checked[current] = True

        cost = costs[current]
        neighbors = graph[current]
        # 이웃 가격 갱신
        for neighbor in neighbors.keys():
            if neighbor not in costs.keys():
                costs[neighbor] = float("inf")
            new_cost = cost + neighbors[neighbor]
            if not checked[neighbor] and new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = current

        current = find_cheapest_node(costs, checked)

    # print(checked.count(True), get_max(costs))


testcase = int(input())
for _ in range(testcase):
    hacking()