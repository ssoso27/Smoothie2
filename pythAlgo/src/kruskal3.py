root = {} # 해당 노드가 속한 트리의 노드
size = {} # 해당 노드의 (자신 포함) 하위 노드 개수


def make_set(nodes):
    for node in nodes:
        root[node] = node
        size[node] = 1


def find_root(v):
    if root[v] != v: # v가 root가 아니면
        root[v] = find_root(root[v])
    return root[v]


def union(root_v, root_u):
    # 트리의 크기가 큰 쪽에 작은 쪽을 붙인다.
    if size[root_v] > size[root_u]:
        root[root_u] = root_v
        size[root_v] += size[root_u]
    else:
        root[root_v] = root_u
        size[root_u] += size[root_v]

    print(root)
    print(size)


def kruskal3(graph):
    minimum_spanning_tree = []

    # 각 정점을 독립 집합으로 만들고
    make_set(graph['vertices'])

    # 엣지를 오름차순으로 정렬하고
    sorted_edge = sorted(graph['edges'], key= lambda edge: edge[0])

    for edge in sorted_edge:
        # 최소 엣지의 양쪽 노드를 꺼내서
        weight, v, u = edge
        # 양쪽 노드의 루트를 비교해서
        root_v = find_root(v)
        root_u = find_root(u)

        # 루트가 다르면 합치고
        if root_v != root_u:
            union(root_v, root_u)
            # 해당 엣지를 최소신장트리에 추가한다
            minimum_spanning_tree.append(edge)

        # 엣지 수가 n-1개가 되면 종료
        if len(minimum_spanning_tree) == (len(root)-1):
            break

    return minimum_spanning_tree



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


print( kruskal3(graph) == result )