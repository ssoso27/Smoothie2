from collections import deque


def make_minorities():
    N = 10000
    is_minority = [True] * N
    is_minority[0] = is_minority[1] = False

    for i in range(2, int(N**0.5)+1):
        for j in range(i+i, N, i):
            is_minority[j] = False

    return [idx for idx in range(1000, N) if is_minority[idx]]


def minority_path2(A, B):
    q = deque()
    checked = [-1] * 10000
    q.append(A)

    while q:
        current = q.popleft()
        for i in range(4):
            for j in range(10):
                next = int(str(current[:i+1]) + str(j) + str(current[i+1]))
                if 1000 <= next < 10000 and next in minorities and checked[next] == -1:
                    checked[next] = checked[current] + 1
                    q.append(next)

    if checked[B] == -1:
        return "impossible"
    else:
        return checked[B]


T = int(input())
minorities = make_minorities()
for _ in range(T):
    A, B = map(int, input().split(" "))
    print(minority_path2(A, B))