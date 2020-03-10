N = int(input())
T = [0] * (N+1)
P = [0] * (N+1)

for i in range(1, N+1):
    T[i], P[i] = map(int, input().split(" "))

# 격자 만들기
grid = [[0]*(N+1) for _ in range(N+1)] # row: 상담, column: 일

# 격자 채우기
for row in range(1, N+1):
    time = T[row]
    price = P[row]
    for col in range(1, N+1):
        previous = max(grid[row-1][col], grid[row][col-1])
        if row+time-1 == col:
            grid[row][col] = max(previous, price + grid[row-1][col-time])
        else:
            grid[row][col] = previous

print(grid[N][N])