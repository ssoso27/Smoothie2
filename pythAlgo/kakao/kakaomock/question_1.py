from collections import deque


def solution(board, moves):
    # 각 열 별 queue 로 만들어두기
    lines = [deque() for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                continue
            lines[j].append(board[i][j])

    # moves 에 맞춰 돌며 인형 뽑기
    picked_dolls = []
    pop_dolls_cnt = 0
    for pick in moves:
        pick = pick-1
        if len(lines[pick]) == 0:
            continue

        doll = lines[pick].popleft()
        if len(picked_dolls) == 0:
            picked_dolls.append(doll)
        else:
            if picked_dolls[len(picked_dolls)-1] == doll:
                # 터치기
                picked_dolls.pop()
                pop_dolls_cnt += 2
            else:
                # 넣기
                picked_dolls.append(doll)
    return pop_dolls_cnt


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))