def solution(tickets):
    answer = []

    # 그래프 만들기
    N = len(tickets)+1
    graph = {}
    for start, end in tickets:
        if start not in graph.keys():
            graph[start] = []
        graph[start].append(end)

    # 그래프 정렬
    for k in graph.keys():
        graph[k] = sorted(graph[k], reverse=True)

    # dfs
    stack = ['ICN']

    while stack:
        airport = stack[-1]

        # 마지막 공항 (이어진 공항이 없을 때)
        if airport not in graph.keys() or len(graph[airport]) == 0:
            stack.pop()
            answer.append(airport)
        else:
            stack.append(graph[airport].pop())

    return answer[::-1]


ex = [
    ([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]], ["ICN", "JFK", "HND", "IAD"]),
    ([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]], ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]),
    ([["ICN", "ATL"], ["ICN", "ATL"], ["ATL", "ICN"], ["ATL", "ICN"]], ["ICN", "ATL", "ICN", "ATL", "ICN"])
]
for t, r in ex:
    print(solution(t) == r)