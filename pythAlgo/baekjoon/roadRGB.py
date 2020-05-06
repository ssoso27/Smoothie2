from sys import stdin
input = stdin.readline

R, G, B = 0, 1, 2
N = int(input())
houses = [[-1, -1, -1] for _ in range(N)]

# 각 집의 색깔 별 가격 입력
for i in range(N):
    houses[i] = list(map(int, input().split(" ")))

dp = [[-1, -1, -1] for _ in range(N)]
dp[0] = houses[0]

# dp 돌리기
for i in range(1, N):
    # i번째 집이 R일 경우 최소 cost
    dp[i][R] = houses[i][R] + min(dp[i-1][G], dp[i-1][B])
    # i번째 집이 G일 경우
    dp[i][G] = houses[i][G] + min(dp[i-1][R], dp[i-1][B])
    # i번째 집이 B일 경우
    dp[i][B] = houses[i][B] + min(dp[i-1][R], dp[i-1][G])

# 최솟값 출력
print(min(dp[N-1]))