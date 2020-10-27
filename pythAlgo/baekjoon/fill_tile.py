from sys import stdin
input = stdin.readline


def solution(N):
    # dp[n] : 3*n 인 타일을 채우는 경우의 수
    # dp[n] = dp[n-2]*dp[2] + dp[n-4]*2 + dp[n-6]*2 + ...
    ## 2 곱하는 이유 : 예외 케이스

    dp = [0 for _ in range(31)]
    dp[0] = 1
    dp[2] = 3

    for i in range(4, N+1, 2):
        dp[i] = dp[i-2] * 3
        for j in range(4, i+1, 2):
            dp[i] += dp[i-j] * 2

    return dp[N]


N = int(input())
print(solution(N))