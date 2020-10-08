def backtracking(idx, order, c, arr):
    # arr 채우기
    arr += order[idx]

    # 다 채웠는지 판단
    if len(arr) == c:
        if arr not in cases[c].keys():
            cases[c][arr] = 0
        cases[c][arr] += 1
        return

    # 다음 백트래킹
    for i in range(idx+1, len(order)):
        backtracking(i, order, c, arr)


def solution(orders, course):
    answer = []

    global cases
    cases = {}
    for c in course:
        cases[c] = {}

    # 순열 만들기
    for order in orders:
        for c in course:
            if len(orders) >= c:
                for i in range(len(order)-c):
                    backtracking(i, order, c, "")

    print(cases)
    # 각 코스요리 뽑아내기
    for c in course:
        max_cnt = 0
        max_cnt_keys = []
        for k in cases[c].keys():
            if cases[c][k] > max_cnt:
                max_cnt = cases[c][k]
                max_cnt_keys = [k]
            elif cases[c][k] == max_cnt:
                max_cnt_keys.append(k)
        answer.append(max_cnt_keys)

    print(sum(sorted(answer), []))
    return sum(sorted(answer), [])


examples = [
    [["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4], ["AC", "ACDE", "BCFG", "CDE"]],
    [["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5], ["ACD", "AD", "ADE", "CD", "XYZ"]],
    [["XYZ", "XWY", "WXA"], [2,3,4], ["WX", "XY"]]
]
for orders, course, result in examples:
    print(solution(orders, course) == result)