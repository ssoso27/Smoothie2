from sys import stdin
input = stdin.readline


def backtracking(idx, S, result, checked):
    # 다 채웠으면
    if idx == len(result):
        print(" ".join(map(str, result)))
        return

    # 첫 숫자가 조건을 벗어나면
    ## ( 첫 숫자의 최댓값은 주어진 배열 S의 K-6+1 번째 요소)
    if idx > 0 and result[0] > S[len(S)-6+1]:
        return

    # idx 보다 적은 수는 나오지 않음
    for i in range(idx, len(S)):
        if checked[i]: # 체크된건 넘김
            continue

        if result[idx-1] > S[i]: # 전 숫자보다 작다면 정렬이 안됨
            continue

        # 정답 리스트에 추가
        checked[i] = True
        result[idx] = S[i]

        # 다음 idx 로 넘어감
        backtracking(idx+1, S, result, checked)

        # 돌아오면 체크 해제
        checked[i] = False
        result[idx] = -1


def lotto(S):
    checked = [False] * len(S)
    result = [-1] * 6

    backtracking(0, S, result, checked)


while True:
    S = list(map(int, input().split(" ")))
    if S.pop(0) == 0:
        break

    lotto(S)
    print()