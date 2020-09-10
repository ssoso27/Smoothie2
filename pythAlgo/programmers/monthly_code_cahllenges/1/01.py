def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            sum = numbers[i] + numbers[j]
            if sum not in answer:
                answer.append(sum)

    return sorted(answer)


numbers = [2,1,3,4,1]
result = [2,3,4,5,6,7]

print(solution(numbers))