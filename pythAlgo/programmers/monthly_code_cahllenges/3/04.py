def have_fake_path(graph):
    return True


def backtracking(cnt, graph, n):
    if cnt == 3:
        return 3

    for i in range(n):
        if i not in graph.keys():
            continue

        if len(graph[i]) == 1: # 가장 말단 노드
            # 그래프에서 해당 노드 지우기
            copy_graph = graph.copy()
            del(copy_graph[i])

            for k in graph.keys():
                if i in graph[k]:
                    if len(copy_graph[k]) == 1:
                        del(copy_graph[k])
                    else:
                        copy_graph[k].remove(i)

            backtracking(cnt-1, copy_graph, n)


def solution(t):
    answer = 0

    graph = {}
    for u, v in t:
        if u not in graph.keys():
            graph[u] = []
        if v not in graph.keys():
            graph[v] = []

        graph[u].append(v)
        graph[v].append(u)

    while len(graph) > 1:
        # 부분 트리 만들기
        backtracking(len(graph), graph, len(graph))

        # have_fake_path(graph)



    print(answer)
    return answer

examples = [
    [[[5,1],[2,5],[3,5],[3,6],[2,4],[4,0]], 7],
    # [[[2,5],[2,0],[3,2],[4,2],[2,1]], 4]
]
for t, r in examples:
    print(solution(t) == r)