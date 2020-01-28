from collections import deque

N = int(input())
G = {}
for n in range(N):
    G[n] = [idx for idx, connected in enumerate(input().split()) if connected == "1"]

search_queue = deque()
result = [["0" for i in range(N)] for j in range(N)]

for i in range(N):
    for j in range(N):
        checked = []
        search_queue.clear()
        search_queue += G[i]
        while search_queue:
            target = search_queue.popleft()
            if target not in checked:
                checked.append(target)
                if target is j:
                    result[i][j] = "1"
                    break
                search_queue += G[target]


for i in range(N):
    print(" ".join(result[i]))