from sys import stdin
input = stdin.readline

N = int(input())
MOD = 10007

dp = [0 for _ in range(N+1)]
dp[0] = 0
dp[1] = 1
if N > 1:
    dp[2] = 2

for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]
    dp[i] %= MOD

print(dp[N])