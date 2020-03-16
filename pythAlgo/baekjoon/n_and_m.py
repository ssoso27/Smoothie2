N, M = map(int, input().split(" "))

check = [False] * (N+1)
result = [0] * M

def backtracking(idx):
    # 다 채우면
    if idx == M:
        # 출력하고 return
        print(" ".join(map(str, result)))
        return

    for i in range(1, N+1):
        if check[i]: # 이미 리스트에 있으면 넘어감
            continue

        # idx 위치에 원소 채우기
        check[i] = True
        result[idx] = i

        # 다음 인덱스 채우러 감
        backtracking(idx+1)

        # 갔다가 돌아오면
        # (?, ..., i, ...) 는 다 채운거니까 해제
        check[i] = False


backtracking(0)