def is_valid(idx, numbers, K):
    if idx >= 1 and abs(numbers[idx] - numbers[idx - 1]) > K:
        return False
    if idx <= len(numbers) - 2 and abs(numbers[idx] - numbers[idx + 1]) > K:
        return False
    return True


def backtracking(target, numbers, K, cnt):
    lst = []
    copy_numbers = numbers.copy()
    for i in range(target+1, len(copy_numbers)):
        # 스와핑
        copy_numbers[target], copy_numbers[i] = copy_numbers[i], copy_numbers[target]

        if is_valid(target, copy_numbers, K) and is_valid(i, copy_numbers, K):
            # 후보 등록
            lst.append(copy_numbers)

    for i in range(len(lst)):
        if not is_valid(i, numbers, K):
             min(backtracking(i, numbers, K, 1), backtracking(i + 1, numbers, K, 1))

def solution(numbers, K):
    answer = -1
    for i in range(len(numbers)):
        if not is_valid(i, numbers, K):
            if i == 0:
                answer = backtracking(i, numbers, K, 1)
            else:
                answer = min(backtracking(i, numbers, K, 1), backtracking(i+1, numbers, K, 1))
            break
    return answer

ex = [
    ([10, 40, 30, 20], 20, 1),
    ([3, 7, 2, 8, 6, 4, 5, 1], 3, 2)
]
for numbers, k, result in ex:
    print(solution(numbers, k) == result)