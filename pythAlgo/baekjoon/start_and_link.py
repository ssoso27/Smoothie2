from sys import stdin
input = stdin.readline

def get_score(team):
    score = 0
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            score += S[team[i]][team[j]] + S[team[j]][team[i]]
    return score


def backtracking(idx, checked, last):
    if idx == N/2:
        # 팀 채우기
        start, link = [], []
        for i in range(N):
            if checked[i]:
                start.append(i)
            else:
                link.append(i)

        # 팀의 능력치 구하기
        global answer
        answer = min(answer, abs(get_score(start) - get_score(link)))
        return

    for i in range(last+1, N):
        checked[i] = True
        backtracking(idx+1, checked, i)
        checked[i] = False


N = int(input())
S = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    S[i] = list(map(int, input().split()))

answer = float('inf')
backtracking(0, [False]*N, -1)

print(answer)