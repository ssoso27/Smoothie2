def solution(numbers, K):
    answer = 0
    return answer


ex = [
    ([10, 40, 30, 20], 20, 1),
    ([3, 7, 2, 8, 6, 4, 5, 1], 3, 2)
]
for numbers, k, result in ex:
    print(solution(numbers, k) == result)