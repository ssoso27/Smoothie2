def solution(tickets):
    # 그래프 만들기
    N = len(tickets)+1
    graph = {}
    for start, end in tickets:
        if start not in graph.keys():
            graph[start] = []
        graph[start].append(end)

    # dfs
    visit = []
    stack = ['ICN']

    while stack:
        airport = stack.pop()
        visit.append(airport)

        if len(visit) == N:
            break

        for next in sorted(graph[airport], reverse=True):
            if [airport, next] in tickets:
                if len(stack) == 0 or (len(stack) > 0 and stack[-1] != next):
                    stack.append(next)
                    tickets.remove([airport, next])
    return visit


ex = [
    ([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]], ["ICN", "JFK", "HND", "IAD"]),
    ([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]], ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]),
    ([["ICN", "ATL"], ["ICN", "ATL"], ["ATL", "ICN"], ["ATL", "ICN"]], ["ICN", "ATL", "ICN", "ATL", "ICN"])
]
for t, r in ex:
    print(solution(t) == r)