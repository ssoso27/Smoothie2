from collections import deque


def solution(n, computers):
    answer = 0
    remain = [i for i in range(n)]

    # 그래프 만들기
    graph = {}
    for i in range(n):
        graph[i] = []

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)

    # bfs
    while remain:
        answer += 1

        q = deque()
        q.append(remain.pop())

        while q:
            pc = q.pop()
            for next in graph[pc]:
                if next in remain:
                    q.append(next)
                    remain.remove(next)

    return answer


ex = [
    (3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2),
    (3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]], 1)
]
for n, c, r in ex:
    print(solution(n, c))