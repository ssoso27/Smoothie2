import math


def is_minority(number):
    for i in range(2, int(math.sqrt(number))+1 ):
        if number % i == 0:
            return False
    return True


# 2 ~ N 의 범위에서 소수들만 거르기
def make_minorities(N):
    is_minority = [True] * N
    for i in range(2, int(N**0.5)+1):
        if is_minority[i]:
            for j in range(i+i, N, i):
                is_minority[j] = False
    return [idx for idx in range(2, N) if is_minority[idx]]


def minority_path(A, B):
    password = A
    cnt = 0
    while password != B:
        changed = False
        cnt += 1
        for i in range(4):
            if password[i:i+1] == B[i:i+1]:
                continue
            new_password = password[:i] + B[i:i+1] + password[i+1:]
            print(cnt, new_password)
            if is_minority(int(new_password)):
                password = new_password
                changed = True
                break
        if not changed:
            return "impossible"
    return cnt


# T = int(input())
# for t in range(T):
#     A, B = input().split(" ")
#     print(minority_path(A, B))