from sys import stdin
input = stdin.readline

MOD = 1000000009
T = int(input())
dp = [[0, 0, 0] for _ in range(100001)]
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]
dp[4] = [2, 0, 1]

for i in range(5, len(dp)):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % MOD
    dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % MOD
    dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % MOD

for _ in range(T):
    print(sum(dp[int(input())]) % MOD)