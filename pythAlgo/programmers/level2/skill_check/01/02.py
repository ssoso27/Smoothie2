def more_bigger(str1, str2):
    for i in range(len(str1)):
        if int(str1[i]) > int(str2[i]):
            return str1
        elif int(str1[i]) < int(str2[i]):
            return str2


def backtracking(idx, n, str_number, numbers):
    if idx == n:
        return str_number

    result = "0"
    for i in range(numbers):
        temp = backtracking(idx+1, n, str_number + str(numbers[i]), numbers[:i].extend(numbers[i+1:]))
        result = more_bigger(temp, result)
    return result


def solution(numbers):
    answer = '0'

    for i in range(len(numbers)):
        result = backtracking(0, len(numbers), str(numbers[i]), numbers[:i].extend(numbers[i+1:]))
        answer = more_bigger(answer, result)

    return answer

ex = {
    [6, 10, 2]: "6210",
    [3, 30, 34, 5, 9]: "9534330"
}

for n, r in ex.items():
    print(solution(n))