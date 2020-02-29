def find_least_node(costs): # 제일 가격이 싼 노드 찾기
    min_cost = float("inf")
    min_cost_node = None
    for node in costs.keys():
        cost = costs[node]
        if node not in proceeds and cost < min_cost:
            min_cost = cost
            min_cost_node = node
    return min_cost_node

testcase = 0
while True:
    testcase += 1
    N = int(input())
    cave = []
    if N == 0:
        break
    for i in range(N):
        cave.append([int(_) for _ in input().split(" ")])

    # 그래프 만들기
    dx = [-1, 0, +1, 0]
    dy = [0, +1, 0, -1]

    graph = {}
    for i in range(N):
        for j in range(N):
            graph[(i, j)] = {}
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x < N and 0 <= y < N:
                    graph[(i, j)][(x, y)] = cave[x][y]

    # 최단 거리 찾기
    proceeds = [(0, 0)] # 처리된 노드 리스트
    parents = {
        (0, 0) : None
    } # 확정된 노드의 부모 노드
    costs = {} # 현재까지의 가격표. (변동 가능)
    costs[(0, 0)] = cave[0][0]
    for node in graph[(0, 0)].keys():
        costs[node] = graph[(0, 0)][node] + costs[(0, 0)]
        parents[node] = (0, 0)

    current = find_least_node(costs)
    while current is not None:
        proceeds.append(current) # 처리 등록
        current_cost = costs[current]

        # 이웃들의 가격 갱신
        neighbors = graph[current]
        for neighbor in neighbors:
            if neighbor not in costs.keys():
                costs[neighbor] = float("inf")

            new_cost = current_cost + neighbors[neighbor]
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = current
        current = find_least_node(costs)

    print("Problem " + str(testcase) + ": " + str(costs[N-1, N-1]))