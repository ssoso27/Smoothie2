from sys import stdin
input = stdin.readline


def get_max_value(num1, num2):
    if len(num1) > len(num2):
        return num1
    elif len(num1) < len(num2):
        return num2
    elif len(num1) == len(num2):
        for i in range(len(num1)):
            if num1[i] > num2[i]:
                return num1
            elif num1[i] < num2[i]:
                return num2

    # 수가 같을 경우
    return num1


strokes = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
N = int(input()) 
grid = [[[-1]] * (N+1) for _ in range(11)]

for r in range(1, 11): # row : 표시할 수 + 1
    target = r - 1
    for c in range(2, N+1): # column : (하위 문제) 획수
        previous = get_max_value(grid[r-1][c], grid[r][c-1])
        if strokes[target] <= c:
            num = [target]
            if grid[r][c-strokes[target]] != [-1]:
                num.extend(grid[r][c-strokes[target]])
            grid[r][c] = get_max_value(previous, num)
        else:
            grid[r][c] = previous

print("".join(map(str, grid[10][N])))