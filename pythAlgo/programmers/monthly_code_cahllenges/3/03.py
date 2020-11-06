def is_star(lst):
    if len(lst) == 2:
        return True

    # 교집합이라고 가정
    commons = lst[0:2]

    for i in range(0, len(lst), 2):
        # 각 집합 내의 숫자가 겹치는지 검사
        if lst[i] == lst[i+1]:
            return False

        # 교집합 검사
        if len(commons) == 2:
            if not (commons[1] == lst[i] or commons[1] == lst[i+1]):
                commons.pop(1)
            if not (commons[0] == lst[i] or commons[0] == lst[i+1]):
                commons.pop(0)

            if len(commons) == 0:
                return False
        else:
            if commons[0] != lst[i] and commons[0] != lst[i+1]:
                return False

    return True


def backtracking(cnt, last, a, subs):
    if cnt > 0 and cnt%2 == 0:
        # 스타 수열인지 확인
        if is_star(subs):
            global answer
            answer = max(answer, cnt)

    if last == len(a):
        return

    for i in range(last+1, len(a)):
        subs.append(a[i])
        backtracking(cnt+1, i, a, subs)
        subs.pop()


def solution(a):
    global answer
    answer = 0

    backtracking(0, -1, a, [])
    print(answer)
    return answer

examples = [
    [[], 0],
    [[0], 0],
    [[5,2,3,3,5,3], 4],
    [[0,3,3,0,7,2,0,2,2,0], 8]
]

for a, r in examples:
    print(solution(a) == r)