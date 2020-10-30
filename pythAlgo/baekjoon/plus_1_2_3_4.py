from sys import stdin
input = stdin.readline

# 순서가 없는 중복 조합

dp = [[1, 0, 0] for _ in range(10001)]
dp[1] = [1, 0, 0]
dp[2] = [1, 1, 0]
dp[3] = [1, 1, 1]
dp[4] = [1, 2, 1]

for i in range(5, len(dp)):
    dp[i][1] = dp[i-2][0] + dp[i-2][1]
    dp[i][2] = dp[i-3][0] + dp[i-3][1] + dp[i-3][2]

T = int(input())
for _ in range(T):
    print(sum(dp[int(input())]))
