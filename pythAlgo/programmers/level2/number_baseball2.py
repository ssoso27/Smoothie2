def solution(baseball):
    answer = 0
    candidate = []
    for i in range(1, 10):
        for j in [n for n in range(1, 10) if n != i]:
            for k in [n for n in range(1, 10) if n != i and n != j]:
                candidate.append( str(i) + str(j) + str(k) )

    # 맞는지 판단
    for ask, s, b in baseball:
        for num in candidate:
            ask = str(ask)

            # 볼 판단
            ball = 0
            for l in range(3):
                for m in range(3):
                    if l == m:
                        continue
                    if num[l] != ask[l]:
                        if (num in candidate):
                            candidate.remove(num)

            # 스트라이크 판단
            strike = 0
            for l in range(3):
                if num[l] != ask[l]:
                    if num in candidate:
                        candidate.remove(num)

    print(candidate)
    return answer


ex = [
    ([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]], 2)
]
for baseball, result in ex:
    print(solution(baseball))