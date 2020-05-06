blocks = {}
blanks = []


def backtracking(idx, filled, blank_idx):
    if idx == len(filled):
        copy_blocks = blocks.copy()
        # 합치기
        for f in filled:
            start = -1
            # 앞 블럭 찾기
            for block in copy_blocks:
                if copy_blocks[block] == f-1:
                    start = block
                    break
            # 블럭 채우기
            ## 앞 블럭이 없는 경우
            if start == -1:
                if f+1 not in copy_blocks.keys():
                    copy_blocks[f] = f
                else:
                    copy_blocks[f] = copy_blocks[f + 1]
            ## 뒷 블럭이 없는 경우
            elif f+1 not in copy_blocks.keys():
                copy_blocks[start] = f
            else:
                copy_blocks[start] = copy_blocks[f + 1]
        print(copy_blocks)
        return

    filled[idx] = blank_idx
    for i in range(blank_idx, len(blanks)):
        backtracking(idx+1, filled, blank_idx+1)



def solution(road, n):
    answer = -1

    # blocks, blanks 채우기
    start = 0
    for idx in range(len(road)):
        if road[idx] == '0':
            blanks.append(idx)
            if start not in blanks:
                blocks[start] = idx - 1
            start = idx + 1
        if idx == len(road)-1 and road[idx] == '1':
            blocks[start] = idx

    backtracking(0, [-1 for _ in range(n)], 0)

    return answer

road = "111011110011111011111100011111"
n = 3
result = 18
print(solution(road, n))
print(solution("001100", 5))