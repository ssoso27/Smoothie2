from sys import stdin
input = stdin.readline


answer = 0
N = int(input())
for i in range(1, N+1):
    nums = []
    while i > 0:
        nums.append(i%10)
        i = i // 10

    is_hansoo = True
    if len(nums) > 1:
        chai = nums[1] - nums[0]
        for j in range(1, len(nums)):
            if nums[j] - nums[j-1] != chai:
                is_hansoo = False
                break

    if is_hansoo:
        answer += 1

print(answer)