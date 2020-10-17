from sys import stdin
input = stdin.readline

N = int(input())
lst = list(map(int, input().split()))
dp = [0 for _ in range(N)]
dp[-1] = lst[-1]

for i in reversed(range(0, N-1)):
    if lst[i] > lst[i+1]:
        for j in range(i+2, N):
            if lst[i] <= lst[j]:
                dp[i] = max(dp[i], lst[i] + dp[j])
        dp[i] = max(lst[i], dp[i+1], dp[i])
    else:
        dp[i] = lst[i] + dp[i+1]




print(max(dp))