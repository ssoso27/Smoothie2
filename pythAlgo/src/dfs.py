def dfs(start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        print(node)
        visited.add(node)
        stack.extend(graph[node])

graph = {
    'A' : {'B', 'C'},
    'B' : {'A', 'D', 'E'},
    'C' : {'A', 'F'},
    'D' : {'B'},
    'E' : {'B', 'F'},
    'F' : {'C', 'E'}
}

dfs('A')