from sys import stdin
input = stdin.readline

n = int(input())
lst = list(map(int, input().split(" ")))

SMALLEST = -987654321
dp = [[SMALLEST]*n for _ in range(n+1)]
dp[1] = lst

max_value = max(lst)
for i in range(2, n+1):
    for j in range(n-i+1):
        dp[i][j] = dp[i-1][j] + dp[1][i-1+j]
        max_value = max(max_value, dp[i][j])

print(max_value)