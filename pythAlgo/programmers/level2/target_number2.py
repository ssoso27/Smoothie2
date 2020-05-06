def solution(numbers, target):
    if not numbers and target == 0: # 끝에 도달하고 target 맞음
        return 1
    elif not numbers: # 끝에 도달하고 target 아님
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])


ex = [
    ([1, 1, 1, 1, 1], 3, 5)
]
for n, t, r in ex:
    print(solution(n, t) == r)