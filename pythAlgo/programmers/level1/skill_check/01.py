def solution(arr):
    answer = []
    before = -1
    for n in arr:
        if before != n:
            answer.append(n)
            before = n

    return answer


ex = [
    ([1,1,3,3,0,1,1], [1, 3, 0, 1]),
    ([4,4,4,3,3], [4,3])
]
for arr, answer in ex:
    print(solution(arr))