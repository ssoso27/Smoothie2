def solution(answer_sheet, sheets):
    answer = -1
    n = len(answer_sheet)

    # 총 의심 문항 수
    for i in range(len(sheets)):
        cheating_point = 0
        max_continual_cnt = 0

        for j in range(len(sheets)):
            all_cnt = 0
            continual_cnt = 0
            last_doubt_idx = -2
            if i == j:
                continue
            # 각 시트 끼리 비교
            for idx in range(n):
                if sheets[i][idx] == sheets[j][idx] and sheets[i][idx] != answer_sheet[idx]:
                    # 연속성 검사
                    if last_doubt_idx+1 == idx:
                        continual_cnt += 1
                    else:
                        continual_cnt = 1
                    all_cnt += 1
                # 가장 긴 연속
                max_continual_cnt = max(max_continual_cnt, continual_cnt)

            # 부정행위 지수 검사
            cheating_point = max(cheating_point, all_cnt + (max_continual_cnt ** 2))
        answer = max(answer, max_continual_cnt)

    return answer


answer_sheet = "4132315142"
sheets = ["3241523133", "4121314445", "3243523133", "4433325251", "2412313253"]
result = 17
print(solution(answer_sheet, sheets))
