def backtracking(idx, current, numbers, target):
    if idx == len(numbers):
        if current == target:
            return 1
        else:
            return 0

    cnt = 0
    cnt += backtracking(idx+1, current+numbers[idx], numbers, target)
    cnt += backtracking(idx+1, current-numbers[idx], numbers, target)
    return cnt


def solution(numbers, target):
    answer = backtracking(0, 0, numbers, target)
    return answer


ex = [
    ([1, 1, 1, 1, 1], 3, 5)
]
for n, t, r in ex:
    print(solution(n, t) == r)