def solution(stones, k):
    answer = 0
    nexts = [i+1 for i in range(len(stones))]
    flag = True

    while flag:
        idx = 0
        while idx < len(stones):
            # 건너지 못하는 돌이면
            if stones[idx] <= 0:
                if nexts[idx] - idx > k:
                    flag = False
                    break
                idx = nexts[idx]

            # 건너편에 도착했으면
            if idx == len(stones):
                answer += 1
                break

            # 밟기
            stones[idx] -= 1

            # 다 닳은 돌 처리
            if stones[idx] == 0:
                nexts[idx] = len(stones)
                for i in range(idx, len(stones)):
                    if stones[i] > 0:
                        nexts[idx] = i
                        break
                for i in range(len(stones)):
                    if nexts[i] == idx:
                        nexts[i] = nexts[idx]
            idx += 1

    return answer


stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))
