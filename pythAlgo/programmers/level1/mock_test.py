def solution(answers):
    answer = []
    soopojas = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    right_cnt = [0 for _ in range(len(soopojas))]

    for a in range(len(answers)):
        for s in range(len(soopojas)):
            if answers[a] == soopojas[s][a % len(soopojas[s])]:
                right_cnt[s] += 1

    max_idx = 0
    for i in range(len(right_cnt)):
        if right_cnt[max_idx] < right_cnt[i]:
            answer = [i+1]
            max_idx = i
        elif right_cnt[max_idx] == right_cnt[i]:
            answer.append(i+1)

    return answer


ex = [
    ([1,2,3,4,5], [1]),
    ([1,3,2,4,2], [1,2,3])
]
for a, r in ex:
    print(solution(a))