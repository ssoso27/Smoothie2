def bfs(start, graph):
    from collections import deque

    distances[start][start] = 0
    q = deque()
    q.append([start, 0])
    while q:
        v, dist = q.popleft()

        for next in graph[v]:
            if distances[start][next] == -1:
                distances[start][next] = dist+1
                q.append([next, dist+1])


def backtracking(last, n):
    if len(lst) == 3:
        # 중간값 구하기
        a, b, c = lst.copy()
        dist = [
            distances[a][b], distances[a][c], distances[b][c]
        ]
        print(lst, dist)#

        dist = sorted(dist)
        global answer
        answer = max(answer, dist[1])
        return

    for i in range(last+1, n+1):
        lst.append(i)
        backtracking(i, n)

        lst.pop()


def solution(n, edges):
    graph = {}
    for i in range(1, n+1):
        graph[i] = []

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # 각 거리 구하기
    global distances
    distances = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n):
        bfs(i, graph)


    # f(a, b, c) 의 a, b, c 조합 구하기
    global lst, answer
    lst = []
    answer = 0
    backtracking(0, n)

    return answer


print(solution(4, [[1,2],[2,3],[3,4]]))