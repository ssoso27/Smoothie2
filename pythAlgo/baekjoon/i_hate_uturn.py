def i_hate_uturn(my_map):
    dx = [-1, +1, 0, 0]
    dy = [0, 0, -1, +1]

    for i in range(R):
        for j in range(C):
            cnt = 0
            if my_map[i][j] == ".":
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]

                    if 0 <= x < R and 0 <= y < C:
                        if my_map[x][y] == ".":
                            cnt += 1
                if cnt is 1:
                    return 1
    return 0


R, C = map(int, input().split(" "))
my_map = []
for i in range(R):
    my_map.append(input())

print(i_hate_uturn(my_map))
