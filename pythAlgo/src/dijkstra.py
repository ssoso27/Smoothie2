def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# 그래프 그리기
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

# 가격 해시테이블
infinity = float("inf") # 무한 (가격을 모르는 정점)
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# (확정 경로의) 부모 해시테이블
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# 이미 처리한 정점 저장
processed = []

# 1. 가장 가격이 싼 정점을 찾는다.
node = find_lowest_cost_node(costs)
while node is not None: # 처리하지 않은 정점이 남아있는동안
    cost = costs[node]
    neighbors = graph[node]
    # 2. 이웃 정점의 가격을 갱신한다.
    for n in neighbors.keys(): # 이 노드의 모든 이웃에 대하여
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost: # 가격이 더 싸면 '확정'
            # 3. 만약 이웃 정점의 가격을 갱신하면 부모도 갱신한다.
            costs[n] = new_cost
            parents[n] = node
    # 4. 해당 정점을 처리했다는 사실을 기록한다.
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(costs["fin"])
n = parents["fin"]
print("fin")
while n is not "start":
    print(n)
    n = parents[n]
print("start")