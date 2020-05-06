from collections import deque


def solution(progresses, speeds):
    answer = []
    last_deploy = -1

    q = deque()
    for i in range(len(progresses)):
        q.append((i, progresses[i], speeds[i]))

    # 개발 시작
    while q:
        # 1일 어치 개발
        deploy_cnt = 0
        for _ in range(len(q)):
            idx, p, s = q.popleft()

            p += s
            if p >= 100 and last_deploy == idx-1: # 개발 완료
                deploy_cnt += 1
                last_deploy = idx
            else:
                q.append((idx, p, s))

        if deploy_cnt != 0:
            answer.append(deploy_cnt)

    return answer


ex = [
    ([91,30,55], [1,30,5], [2,1]),
    ([50,50,50], [10,20,30], [3]),
    ([50,50,50], [30,10,30], [1,2]),
    ([0,0,0], [50,50,50], [3])
]
for p, s, r in ex:
    print(solution(p, s) == r)