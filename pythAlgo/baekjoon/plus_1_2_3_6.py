from sys import stdin
input = stdin.readline

MOD = 1000000009
T = int(input())
dp = [0 for _ in range(100001)]
dp[1] = 1
dp[2] = 2
dp[3] = 2
dp[4] = 3
dp[5] = 3
dp[6] = 6

for i in range(7, len(dp)):
    dp[i] = (dp[i-2] + dp[i-4] + dp[i-6]) % MOD

for _ in range(T):
    print(dp[int(input())] % MOD)