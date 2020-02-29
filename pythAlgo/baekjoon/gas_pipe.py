R, C = map(int, input().split(" "))
europe = []
for _ in range(R):
    europe.append(input())

M = (-1, -1)
Z = (-1, -1)
dead_end = (-1, -1)

dx = [-1, 0, +1, 0]
dy = [0, +1, 0, -1]
weight = [1, 2, 3, 5]
blocks = ["|", "-", "+", "1", "2", "3", "4"]
totals = [4, 7, 11, 5, 3, 6, 8]
directions = {
    "|" : [0, 2],
    "-" : [1, 3],
    "+" : [0, 1, 2, 3],
    "1" : [1, 2],
    "2" : [0, 1],
    "3" : [0, 3],
    "4" : [2, 3]
}

# 그래프 그리기
graph = {}
for i in range(R):
    for j in range(C):
        if europe[i][j] == ".":
            continue
        elif europe[i][j] == "M":
            M = (i, j)
        elif europe[i][j] == "Z":
            Z = (i, j)
        else:
            for block in blocks:
                if europe[i][j] == block:
                    graph[(i, j)] = []
                    for direction in directions[block]:
                        x = i + dx[direction]
                        y = j + dy[direction]
                        if 0 <= x < R and 0 <= y < C:
                            if europe[x][y] == ".":
                                dead_end = (x, y)
                            else:
                                graph[(i, j)].append((x, y))
                    break

# 막다른 길의 이웃 조사
total = 0
for i in range(4):
    x = dead_end[0] + dx[i]
    y = dead_end[1] + dy[i]
    if 0 <= x < R and 0 <= y < C:
        if i == 0 and europe[x][y] in [blocks[0], blocks[2], blocks[3], blocks[6]]:
            total += weight[i]
        elif i == 1 and europe[x][y] in [blocks[1], blocks[2], blocks[5], blocks[6]]:
            total += weight[i]
        elif i == 2 and europe[x][y] in [blocks[0], blocks[2], blocks[4], blocks[5]]:
            total += weight[i]
        elif i == 3 and europe[x][y] in [blocks[1], blocks[2], blocks[3], blocks[4]]:
            total += weight[i]

# 필요 블럭 판별
print(dead_end[0]+1, dead_end[1]+1, blocks[totals.index(total)])