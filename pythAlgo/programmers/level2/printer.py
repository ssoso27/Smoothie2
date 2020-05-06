from collections import deque


def solution(priorities, location):
    # 인쇄 대기 목록 큐
    q = deque()
    for i in range(len(priorities)):
        q.append((i, priorities[i]))

    # 중요도 배열
    weights = sorted(priorities, reverse=True)

    # 프린트
    cnt = 0
    while q:
        idx, p = q.popleft()
        if p == weights[0]:
            cnt += 1
            weights.pop(0)
            if idx == location:
                return cnt
        else:
            q.append((idx, p))


ex = [
    ([2, 1, 3, 2], 2, 1),
    ([1, 1, 9, 1, 1, 1], 0, 5)
]
for p, l, r in ex:
    print(solution(p, l))