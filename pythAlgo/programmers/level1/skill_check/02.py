def make_prime_numbers(n):
    prime_numbers = [True for _ in range(n+1)]
    prime_numbers[0] = False
    prime_numbers[1] = True
    for i in range(2, int(n**0.5)+1):
        # 해당 소수의 배수들을 뺌
        if prime_numbers[i]:
            m = 2
            while True:
                target = i*m
                if target > n:
                    break
                prime_numbers[target] = False
                m += 1

    return prime_numbers


def solution(n):
    answer = 0
    prime_numbers = make_prime_numbers(n)

    for i in range(2, n+1):
        if prime_numbers[i]:
            answer += 1

    return answer


ex = [
    (10, 4),
    (5, 3)
]
for n, result in ex:
    print(solution(n))