def solution(brown, red):
    answer = []

    # red의 약수 구하기
    for i in range(1, int(red**0.5)+1):
        if red % i == 0:
            j = red // i
            if brown == ((i + 2) * 2) + ((j + 2) * 2) - 4:
                answer = [j+2, i+2]
                break

    return answer


ex = [
    (10, 2, [4,3]),
    (8, 1, [3,3]),
    (24, 24, [8,6])
]
for brown, red, result in ex:
    print(solution(brown, red) )