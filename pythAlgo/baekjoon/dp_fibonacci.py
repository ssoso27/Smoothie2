from sys import stdin
input = stdin.readline

cnt_zero = [0 for _ in range(41)]
cnt_one = [0 for _ in range(41)]
cnt_zero[0] = 1
cnt_one[1] = 1
idx = 1

T = int(input())
for _ in range(T):
    N = int(input())
    while idx < N:
        idx += 1
        cnt_zero[idx] = cnt_zero[idx-1] + cnt_zero[idx-2]
        cnt_one[idx] = cnt_one[idx-1] + cnt_one[idx-2]

    print(cnt_zero[N], cnt_one[N])
