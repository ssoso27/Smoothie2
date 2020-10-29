from sys import stdin
input = stdin.readline

MOD = 1000000009
T = int(input())
dp = [0 for _ in range(1000001)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

last = 3
for _ in range(T):
    n = int(input())
    if dp[n] == 0:
        for i in range(last+1, n+1):
            dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % MOD
        last = n

    print(dp[n])