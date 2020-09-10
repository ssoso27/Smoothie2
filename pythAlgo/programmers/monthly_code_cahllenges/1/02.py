def solution(n):
    BOTTOM, RIGHT, DIAGONAL = 0, 1, 2
    direction = BOTTOM
    blocks = 0

    answer = []
    for i in range(1, n+1):
        answer.append([0 for j in range(i)])
        blocks += i

    r, c = 0, 0
    # block을 차례로 채워나간다.
    for num in range(1, blocks+1):
        answer[r][c] = num

        if direction == BOTTOM and (r == n-1 or answer[r+1][c] != 0):
            direction = RIGHT
        elif direction == RIGHT and (c == n-1 or answer[r][c+1] != 0):
            direction = DIAGONAL
        elif direction == DIAGONAL and answer[r-1][c-1] != 0:
            direction = BOTTOM

        if direction == BOTTOM:
            r += 1
        elif direction == RIGHT:
            c += 1
        elif direction == DIAGONAL:
            r -= 1
            c -= 1

    answer = sum(answer, [])
    return answer


results = [
    [1,2,9,3,10,8,4,5,6,7],
    [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9],
    [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
]

for i in range(4, 7):
    print(results[i-4] == solution(i))
