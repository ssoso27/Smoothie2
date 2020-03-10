roots = {}
sizes = {}

def make_roots(n):
    for i in range(1, n+1):
        roots[i] = i
        sizes[i] = 1


def find_root(node):
    target = node
    while roots[target] != target:
        target = roots[target]
    return target


def union(root1, root2):
    if sizes[root1] > sizes[root2]:
        # root1에 root2를 합친다.
        roots[root2] = root1
        sizes[root1] += sizes[root2]
    else:
        # root2에 roo1을 합친다.
        roots[root1] = root2
        sizes[root2] += sizes[root1]


def is_tree(nodes):
    standard_root = roots[nodes.pop()]
    while nodes:
        if standard_root != roots[nodes.pop()]:
            return False
    return True

def diameter_of_tree(n, edges):
    selected_nodes = set()
    diameter = 0
    # 각 정점을 독립 트리화 하고
    make_roots(n)
    for edge in edges:
        # 엣지의 양 끝 노드를 가져와서
        v, u, weight = edge
        # 루트를 확인하고
        root1 = find_root(v)
        root2 = find_root(u)
        # 트리가 다르면 합친다
        if root1 != root2:
            union(root1, root2)
            selected_nodes.add(v)
            selected_nodes.add(u)
            diameter += weight

        if is_tree(selected_nodes):
            break
    print(selected_nodes)

    return diameter


n = int(input())
edges = []
for _ in range(n-1):
    edges.append(tuple(map(int, input().split(" "))))

edges.sort(key=lambda x: x[2], reverse=True)
print(diameter_of_tree(n, edges))