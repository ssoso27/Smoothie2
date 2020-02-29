graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['end'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['end'] = 5
graph['end'] = {}

infinity = float("inf") # 무한 (가격을 모르는 정점)
prices = {}
prices['a'] = 6
prices['b'] = 2
prices['end'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['end'] = None

processed = []

def find_least_node(p):
    return 1

node = find_least_node(prices)
while node is not None:
    processed.append(node)
    current_price = prices[node]
    neighbors = graph[node]

    for neighbor in neighbors.keys():
        new_price = current_price + neighbors[neighbor]
        if new_price < prices[neighbor]:
            prices[neighbor] = new_price
            parents[neighbor] = node

    node = find_least_node(prices)