def quadtree(S):
    n = len(S)
    half = n // 2
    SS = [[] for _ in range(4)]

    for i in range(n):
        if i < half:
            SS[0].append(S[i][ :half])
            SS[1].append(S[i][half: ])
        else:
            SS[2].append(S[i][ :half])
            SS[3].append(S[i][half: ])
    print(SS)#

    for s in SS:
        is_divided = False
        first = s[0][0]
        for i in range(half):
            for j in range(half):
                if s[i][j] != first:
                    # 분할
                    quadtree(s.copy())
                    is_divided = True
                    break
            if is_divided:
                break

        # 전부 같은 숫자면 압축
        if not is_divided:
            answer[first] += 1
            print("압축 " + str(s))


def solution(arr):
    global answer
    answer = [0, 0]

    is_same = True
    first = arr[0][0]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != first:
                is_same = False
                break
        if not is_same:
            break

    if is_same:
        answer[first] += 1
    else:
        quadtree(arr)

    return answer


print(solution([[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]))