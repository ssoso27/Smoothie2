def solution(arrangement):
    answer = 0
    bar_cnt = 0
    last_str = ""

    for s in arrangement:
        # 쇠막대기 시작
        if s == "(":
            bar_cnt += 1
        elif s == ")":
            if last_str == "(": # 레이저
                bar_cnt -= 1
                answer += bar_cnt
            else: # 쇠막대기 끝
                answer += 1
                bar_cnt -= 1
        last_str = s

    return answer

ex = [
    ("()(((()())(())()))(())", 17)
]
for a, r in ex:
    print(solution(a))