from collections import deque

def solution(v):
    dd = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    n = len(v)
    answer = [0, 0, 0]
    visited = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                target = v[i][j]
                answer[target] += 1

                q = deque()
                q.append([i, j])

                # bfs 로 영역 찾기
                while q:
                    x, y = q.popleft()

                    for dx, dy in dd:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and v[nx][ny] == target:
                            q.append([nx, ny])
                            visited[nx][ny] = True

    return answer

print(solution([[0,0,1,1],[1,1,1,1],[2,2,2,1],[0,0,0,2]]	))
print(solution([[0,0,1],[2,2,1],[0,0,0]]))