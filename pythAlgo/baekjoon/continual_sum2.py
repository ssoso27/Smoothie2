from sys import stdin
input = stdin.readline

n = int(input())
lst = list(map(int, input().split(" ")))

answer = max(lst)
for cnt in range(2, n + 1):
    sum_value = sum(lst[:cnt])
    for end in range(cnt-1, n):
        if end != cnt-1:
            sum_value = sum_value - lst[end-cnt] + lst[end]
        answer = max(answer, sum_value)

print(answer)
