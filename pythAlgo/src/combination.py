result = []

def backtracking(idx, n, last_selected, maken, arr):
    global result
    if idx == n:
        result.append(maken.copy())

    # 순서를 강제 -> 마지막으로 선택된 요소의 뒷요소만 가능
    for i in range(last_selected + 1, len(arr)):
        # 조합에 요소 추가
        maken.append(arr[i])

        # 다음 요소를 찾아 tracking
        backtracking(idx+1, n, i, maken, arr)

        # 돌아온 후, 추가한 요소 제거
        maken.pop()

# arr 에서 n개의 원소의 조합을 찾는 함수
def combination(arr, n):
    maken = []
    backtracking(0, n, -1, maken, arr)
    print(result)


combination(["a","b","c","d"], 2)