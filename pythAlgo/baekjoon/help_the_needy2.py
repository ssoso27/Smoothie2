N = int(input())

roots = {}
sizes = {}
edges = []


def make_egdes():
    total_weight = 0
    for i in range(N):
        row = input()
        for j in range(N):
            if ord('a') <= ord(row[j]) <= ord('z'):
                weight = ord(row[j]) - ord('a') + 1
            elif ord('A') <= ord(row[j]) <= ord('Z'):
                weight = ord(row[j]) - ord('A') + 27
            else:
                weight = 0

            if weight != 0:
                edges.append((weight, i, j))
                total_weight += weight
    return total_weight


def make_roots():
    for i in range(N):
        roots[i] = i
        sizes[i] = 1


def find_root(v):
    # if v != roots[v]:
    #     return find_root(roots[v])
    # return roots[v]
    while v != roots[v]:
        v = roots[v]
    return roots[v]


def union(v_root, u_root):
    if sizes[v_root] < sizes[u_root]:
        roots[v_root] = u_root
        sizes[u_root] += sizes[v_root]
    else:
        roots[u_root] = v_root
        sizes[v_root] += sizes[u_root]


def kruskal():
    minimum_spanning_tree = []

    # 각 정점을 독립 집합화 하고
    make_roots()

    # 엣지를 오름차순 정렬하고
    sorted_edges = sorted(edges, key = lambda edge: edge[0])

    for edge in sorted_edges:
        # 최소 엣지의 양끝노드를 꺼내서
        weight, v, u = edge

        # 루트가 다르면
        v_root         = find_root(v)
        u_root = find_root(u)

        if v_root != u_root:
            # 합친다
            union(v_root, u_root)
            # 그리고 mst에 추가한다
            minimum_spanning_tree.append(edge)

        # mst의 크기가 N-1이면 종료
        if len(minimum_spanning_tree) == N-1:
            break

    if len(minimum_spanning_tree) < N-1: # 트리가 만들어지지 않음
        return -1
    else:
        return minimum_spanning_tree




total_weight = make_egdes()
mst = kruskal()

if mst == -1:
    print(mst)
else:
    sum = 0
    for edge in mst:
        sum += edge[0]

    print(total_weight - sum)