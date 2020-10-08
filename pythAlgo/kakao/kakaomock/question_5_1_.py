parents = []


def find_next_stone(stone):
    if parents[stone] != stone:
        parents[stone] = find_next_stone(parents[stone])

    return parents[stone]


def solution(stones, k):
    global parents
    answer = 0
    flag = True

    # for i in range(len(stones)+1):
    #     parents[i] = i
    parents = [i for i in range(len(stones)+1)]

    while flag:
        i = 0
        while i < len(stones):
            # 밟을 돌이 다 닳아있으면
            if stones[i] == 0:
                next = find_next_stone(i)
                # 거리가 너무 멀면
                if next - i >= k:
                    flag = False
                    break
                # 다 건너갈 수 있으면
                if next == len(stones):
                    answer += 1
                    break

                i = next

            # 정상적으로 밟음
            stones[i] -= 1
            # 돌이 다 닳으면
            if stones[i] == 0:
                parents[i] = parents[i+1]
                if parents[i] - i > k:
                    flag = False
                    break

            # 다 건넜으면
            if i + 1 == len(stones):
                answer += 1
                break

            i += 1


    return answer


stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))