from sys import stdin
from collections import deque
input = stdin.readline

C, B = map(int, input().split(" "))
cony = C

brown_visited = [[False] * 2 for _ in range(200001)]
cony_time = 0
q = deque()
q.append((B, 0))

while True: # 1바퀴 = 코니 1 time
    # 코니 이동
    cony += cony_time

    # 코니가 탈주함
    if cony > 200000:
        print(-1)
        break

    # 코니가 잡힘
    if 0 <= cony <= 200000 and brown_visited[cony][cony_time % 2]:
        print(cony_time)
        break

    # 해당 level 의 노드에 대해 돌림
    for i in range(len(q)):
        brown_position, brown_time = q.popleft()
        new_time = (brown_time + 1) % 2

        for new_position in [brown_position-1, brown_position+1, brown_position*2]:
            if 0 <= new_position <= 200000 and not brown_visited[new_position][new_time]:
                brown_visited[new_position][new_time] = True
                q.append((new_position, new_time))

    cony_time += 1