answer = []

 
def backtracking(idx, n, maken, used, arr):
    global answer
    # 순열 완성
    if idx == n:
        answer.append(maken.copy())
        return

    for i in range(len(arr)):
        if not used[i]:
            # 순열에 요소 추가
            maken.append(arr[i])
            used[i] = True

            # 다음 요소를 찾아 tracking
            backtracking(idx+1, n, maken, used, arr)

            # 돌아온 후, 추가한 요소 제거
            maken.pop()
            used[i] = False


# arr 에서 n개를 뽑아 순열 만들기
def permutation(arr, n):
    maken = [] # 만들어진 순열
    used = [False for _ in range(len(arr))] # 이 요소가 들어갔는지 판별용
    backtracking(0, n, maken, used, arr)
    print(answer)


permutation(["a","b","c","d"], 2)