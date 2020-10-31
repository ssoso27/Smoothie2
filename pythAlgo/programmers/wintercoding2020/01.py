def my_replace(str, idx, ch):
    return ''.join(str[:idx] + ch + str[idx+1:])

def solution(n, delivery):
    answer = '?'*n
    fails = []

    for x, y, d in delivery:
        if d == 1:
            answer = my_replace(answer, x-1, 'O')
            answer = my_replace(answer, y-1, 'O')
        elif d == 0:
            # 둘 중 하나가 O 면 나머지는 무조건 X
            if answer[x-1] == 'O':
                answer = my_replace(answer, y-1, 'X')
            elif answer[y-1] == 'O':
                answer = my_replace(answer, x-1, 'X')

            # 둘 중 하나가 X면 나머지는 O 또는 X 또는 ?
            elif answer[x-1] == 'X':
                if answer[y-1] == '?':
                    fails.append([x-1, y-1])
            elif answer[y-1] == 'X':
                if answer[x-1] == '?':
                    fails.append([x-1, y-1])

            # 둘 다 ?면 모른다.
            elif answer[x-1] == '?' and answer[y-1] == '?':
                fails.append([x-1, y-1])

    # fails 돌리기
    isChange = True
    while isChange:
        for i in range(len(fails)):
            x, y = fails[i]
            isChange = False
            if answer[x] == 'O':
                answer = my_replace(answer, y, 'X')
                isChange = True
            elif answer[y] == 'O':
                answer = my_replace(answer, x, 'X')
                isChange = True

    return ''.join(answer)

print(solution(6, [[1,3,1],[3,5,0],[5,4,0],[2,5,0]]))
print(solution(7, [[5,6,0],[1,3,1],[1,5,0],[7,6,0],[3,7,1],[2,5,0]]))