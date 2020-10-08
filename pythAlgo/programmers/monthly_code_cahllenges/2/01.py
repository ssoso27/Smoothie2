def solution(n):
    answer = 0
    # 1. 삼진법 구하기
    ternary = ''
    while n > 0:
        ternary = str(n % 3) + ternary
        n = n // 3

    # 2. 삼진법 거꾸로
    ternary = ternary[::-1]

    # 3. 십진수로
    for i in range(len(ternary)):
        answer += int(ternary[len(ternary)-1-i]) * (3 ** i)

    return answer

print(solution(45))