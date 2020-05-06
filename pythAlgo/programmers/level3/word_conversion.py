from collections import deque


def solution(begin, target, words):
    answer = 0
    words = [begin] + words
    end = -1

    # words 에 target 이 있는지 확인
    if target not in words:
        return 0
    else:
        end = words.index(target)


    # 그래프 만들기
    graph = {}
    for i in range(len(words)):
        graph[i] = []

    for i in range(len(words)):
        for j in range(1, len(words)):
            if i == j:
                continue

            # 이어질 수 있는 단어인지 체크
            incorrect_cnt = 0
            for k in range(len(words[i])):
                if words[i][k] != words[j][k]:
                    incorrect_cnt += 1

            # 한 글자만 다르면 이어줌
            if incorrect_cnt == 1:
                graph[i].append(j)

    # bfs
    visited = [False for _ in range(len(words))]
    visited[0] = True

    q = deque()
    q.append((0, 0))

    while q:
        depth, word = q.popleft()

        for next in graph[word]:
            if next == end:
                return depth+1

            if not visited[next]:
                visited[next] = True
                q.append((depth + 1, next))

    return answer

ex = [
    ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 4),
    ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0)
]
for b, t, w, r in ex:
    print(solution(b, t, w))