def make_trees(nodes):
    node_set = set(nodes)
    trees = {}

    for node in node_set:
        trees[node] = {}

    return trees


def get_tree(trees, node):


    pass


def find_root_node(trees, tree):
    pass


def merge_tree(trees, left_root, right_root):
    pass


def kruscal(graph):
    number_of_node = len(graph['nodes'])

    # 모든 정점을 독립적인 집합으로 만든다
    trees = make_trees(graph['nodes'])
    # 간선을 비용 오름차순으로 정렬한다
    sorted_edges = sorted(graph['edges'], key=lambda edge: edge[0])

    while len(trees.keys()) < number_of_node:
        # 비용이 최소인 간선의 양 끝 정점을 찾는다
        cost, left_node, right_node = sorted_edges.pop(0)

        # 해당 정점이 속한 트리의 루트 정점을 찾는다.
        left_tree = get_tree(trees, left_node)
        right_tree = get_tree(trees, right_node)

        left_root = find_root_node(trees, left_tree)
        right_root = find_root_node(trees, right_tree)

        # 두 정점의 루트 정점이 다른지 확인한다.
        if left_root == right_node:
            continue

        # 루트 정점이 다를 경우, 두 트리를 합친다.
        merge_tree(trees, left_root, right_root)

    # 만들어진 최종 트리를 return 한다.
    return trees


graph = {
'nodes': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
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

result = [
    (5, 'A', 'D'),
    (5, 'C', 'E'),
    (6, 'D', 'F'),
    (7, 'A', 'B'),
    (7, 'B', 'E'),
    (9, 'E', 'G')
]

print(kruscal(graph) == result)
