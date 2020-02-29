parent = {} # 노드의 최상위 부모
rank = {} # depth

# 정점을 독립적인 집합으로 만든다
def make_set(v):
    parent[v] = v # root의 최상위 부모는 자기자신
    rank[v] = 0 # root의 depth는 0


# 해당 정점의 최상위 정점을 찾는다
def find(v):
    if parent[v] != v: # v가 root가 아니면
        parent[v] = find(parent[v]) #

    return parent[v]

# 두 정점을 연결한다
def union(v, u):
    root1 = find(v)
    root2 = find(u)

    if root1 != root2:
        # 짧은 트리의 루트가 긴 트리의 루트를 가리키게 만드는 것이 좋다.
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2

        if rank[root1] == rank[root2]:
            rank[root2] += 1
    print("----")
    print(parent)
    print(rank)

def kruskal2(graph):
    for v in graph['vertices']:
        make_set(v)

    mst = []

    edges = graph['edges']
    edges.sort()

    for edge in edges:
        weight, v, u = edge

        if find(v) != find(u):
            union(v, u)
            mst.append(edge)

    return mst


graph = {
'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
'edges': [
    (7, 'A', 'B'),
    (5, 'A', 'D'),
    (7, 'B', 'A'),
    (8, 'B', 'C'),
    (9, 'B', 'D'),
    (7, 'B', 'E'),
    (8, 'C', 'B'),
    (5, 'C', 'E'),
    (5, 'D', 'A'),
    (9, 'D', 'B'),
    (7, 'D', 'E'),
    (6, 'D', 'F'),
    (7, 'E', 'B'),
    (5, 'E', 'C'),
    (15, 'E', 'D'),
    (8, 'E', 'F'),
    (9, 'E', 'G'),
    (6, 'F', 'D'),
    (8, 'F', 'E'),
    (11, 'F', 'G'),
    (9, 'G', 'E'),
    (11, 'G', 'F'),
    ]
}

result = [(5, 'A', 'D'),
 (5, 'C', 'E'),
 (6, 'D', 'F'),
 (7, 'A', 'B'),
 (7, 'B', 'E'),
 (9, 'E', 'G')]


print( kruskal2(graph) == result )