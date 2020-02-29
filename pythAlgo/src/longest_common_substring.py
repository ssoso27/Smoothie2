str1 = "helloworldsohee"
str2 = "hesworldllo"

# 격자 만들기
dp = [[-1] * len(str1) for _ in range(len(str2))]

for row in range(len(str2)):
    for column in range(len(str1)):
        if str1[column] != str2[row]:
            dp[row][column] = 0
            continue
        else:
            if 0 <= row-1 < len(str2) and 0 <= column-1 < len(str1):
                dp[row][column] = dp[row - 1][column - 1] + 1
            else:
                dp[row][column] = 1
print(dp)

max = 0
for row in dp:
    for cell in row:
        if max < cell:
            max = cell
print(max)