def solution(baseball):
    candidate = []

    # 모든 조합 찾기
    for i in range(1, 10):
        for j in [n for n in range(1, 10) if n != i]:
            for k in [n for n in range(1, 10) if n != i and n != j]:
                num = str(i) + str(j) + str(k)
                candidate.append(num)

                # 제시된 조건과 비교
                for ask, s, b in baseball:
                    ask = str(ask)

                    strike = 0
                    ball = 0
                    for m in range(3):
                        # 스트라이크 비교
                        if ask[m] == num[m]:
                            strike += 1

                        # 볼 비교
                        if ask[m] == num[(m+1)%3] or ask[m] == num[(m+2)%3]:
                            ball += 1

                    # 후보군에서 빼기
                    if not (strike == s and ball == b):
                        candidate.remove(num)
                        break

    return len(candidate)


ex = [
    ([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]], 2)
]
for baseball, result in ex:
    print(solution(baseball))