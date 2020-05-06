def solution(office, r, c, move):
    N, E, S, W = 0, 1, 2, 3
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    answer = 0
    direction = N

    # 첫 자리 청소
    answer += office[r][c]
    office[r][c] = 0

    for m in move:
        if m == "go":
            nr, nc = r + dr[direction], c + dc[direction]
            if 0 <= nr < len(office) and 0 <= nc < len(office):
                if office[nr][nc] != -1:
                    # 청소 수행
                    answer += office[nr][nc]
                    office[nr][nc] = 0
                    r, c = nr, nc

        elif m == "right":
            direction = (direction + 1) % 4

        elif m == "left":
            direction = (direction - 1 + 4) % 4

    return answer


ex = [
    ([[5,-1,4],[6,3,-1],[2,-1,1]], 1, 0, ["go","go","right","go","right","go","left","go"], 14)
]
for office, r, c, move, result in ex:
    print(solution(office, r, c, move) == result)