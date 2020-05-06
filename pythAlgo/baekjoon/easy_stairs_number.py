from sys import stdin
input = stdin.readline

NANUGE = 1000000000
N = int(input())

# 격자 틀 만들기
dp = [[-1 for _ in range(10)] for _ in range(N+1)]
dp[1] = [1 for _ in range(10)]

# 격자 채우기
for i in range(2, N+1):
    for start_number in range(10):
        if start_number == 0: # 길이가 i, 0으로 시작하는 숫자
            dp[i][start_number] = dp[i-1][start_number+1]
        elif start_number == 9: # 길이가 i, 9로 시작하는 숫자
            dp[i][start_number] = dp[i-1][start_number-1]
        else: # 길이가 i인 숫자
            dp[i][start_number] = dp[i-1][start_number-1] + dp[i-1][start_number+1]


# 0으로 시작하는 숫자는 제외하고 출력
print(sum(dp[N][1:]) % NANUGE)