from sys import stdin
input = stdin.readline

MOD = 1000000009
N = 100001
T = int(input())
dp = [[0, 0] for _ in range(N)]
dp[1][0], dp[1][1] = 0, 1
dp[2][0], dp[2][1] = 1, 1
dp[3][0], dp[3][1] = 2, 2
dp[4][0], dp[4][1] = 4, 3

for i in range(5, N):
    dp[i][0] = (dp[i-1][1] + dp[i-2][1] + dp[i-3][1]) % MOD
    dp[i][1] = (dp[i-1][0] + dp[i-2][0] + dp[i-3][0]) % MOD

for _ in range(T):
    n = int(input())
    print(str(dp[n][1]) + " " + str(dp[n][0]))
