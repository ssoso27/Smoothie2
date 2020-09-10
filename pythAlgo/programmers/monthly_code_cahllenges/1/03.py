def solution(a):
    # 규칙 1) [최솟값이 있는 배열] N [N보다 작은 수가 있는 배열] 이면 불가능
    # 규칙 2) 각 배열의 처음과 끝 원소는 항상 가능
    # 규칙 3) 최솟값은 항상 가능

    # 1. 최솟값 찾기
    min_idx = 0
    for i in range(1, len(a)):
        if a[i] < a[min_idx]:
            min_idx = i

    # 2. 불가능한 케이스 찾아서 빼기
    answer = len(a)
    left_min_val, right_min_val = 1000000001, 1000000001

    # 2-1. 최솟값 기준 왼쪽 부터
    for idx in range(1, min_idx): # 처음, 끝 원소는 항상 가능
        if idx == min_idx:
            continue

        if idx < min_idx:
            # 왼쪽 배열 최솟값 갱신
            if a[idx-1] < left_min_val:
                left_min_val = a[idx-1]
            # 가능한지 비교
            if a[idx] > left_min_val:
                answer -= 1

    # 2-2. 최솟값 기준 오른쪽 부터
    for idx in range(len(a)-2, min_idx, -1):
        if idx == min_idx:
            continue

        if idx > min_idx:
            # 오른쪽 배열 최솟값 갱신
            if a[idx+1] < right_min_val:
                right_min_val = a[idx+1]
            # 가능한지 비교
            if a[idx] > right_min_val:
                answer -= 1

    return answer

#
# examples = [
#     ([9,-1,-5], 3),
#     ([-16,27,65,-2,58,-92,-71,-68,-61,-33], 6)
# ]
# for a, r in examples:
#     print(solution(a) == r)
solution([-16,27,65,-2,58,-92,-71,-68,-61,-33])