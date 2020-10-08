def backtracking(idx, order, arr, c):
    arr += order[idx]

    if len(arr) == c:
        arr = "".join(sorted(arr))
        if arr not in cases[c].keys():
            cases[c][arr] = 0
        cases[c][arr] += 1

    for i in range(idx+1, len(order)):
        backtracking(i, order, arr, c)


def solution(orders, course):
    answer = []

    global cases
    cases = {}
    for c in course:
        cases[c] = {}

    # 순열 찾기
    for order in orders:
        for c in course:
            for i in range(len(order)-c+1):
                backtracking(i, order, "", c)

    # 각 코스별 최다 카운트 구하기
    for c in course:
        max_cnt = 0
        max_cnt_key = []

        for k in cases[c].keys():
            if cases[c][k] > max_cnt:
                max_cnt = cases[c][k]
                max_cnt_key = [k]
            elif cases[c][k] == max_cnt:
                max_cnt_key.append(k)

        # 2명 이상인지 확인
        if max_cnt >= 2:
            answer.extend(max_cnt_key)

    return sorted(answer)


examples = [
    [["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4], ["AC", "ACDE", "BCFG", "CDE"]],
    [["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5], ["ACD", "AD", "ADE", "CD", "XYZ"]],
    [["XYZ", "XWY", "WXA"], [2,3,4], ["WX", "XY"]]
]
for orders, course, result in examples:
    print(solution(orders, course) == result)