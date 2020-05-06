def solution(answer_sheet, sheets):
    answer = -1
    n = len(answer_sheet)

    for i in range(len(sheets)):
        cheating_point = 0
        for j in range(len(sheets)):
            if i == j:
                continue

            last_doubt_idx = -2
            all_doubt = 0
            continual_doubt = 0
            max_continual = 0

            # 각 문항마다 돌며 의심 문항 체크
            for idx in range(n):
                if sheets[i][idx] == sheets[j][idx] and sheets[i][idx] != answer_sheet[idx]:
                    if last_doubt_idx == idx - 1:  # 연속성 체크
                        continual_doubt += 1
                    else:
                        continual_doubt = 1

                    all_doubt += 1
                    last_doubt_idx = idx
                    max_continual = max(max_continual, continual_doubt)

            # 부정행위 의심 지수 체크
            cheating_point = max(cheating_point, all_doubt + (max_continual ** 2))
        answer = max(cheating_point, answer)
    return answer


answer_sheet = "4132315142"
sheets = ["3241523133", "4121314445", "3243523133", "4433325251", "2412313253"]
result = 17
print(solution(answer_sheet, sheets))
print(solution("53241", ["53241", "42133", "53241", "14354"]))
print(solution("24551", ["24553", "24553", "24553", "24553"]))
