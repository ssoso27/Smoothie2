def solution(s):
    answer = [0, 0]

    while s != "1":
        # 1. 모든 0 제거 = 1의 개수 세기
        cnt = 0
        for i in range(len(s)):
            if s[i] == "1":
                cnt += 1
        answer[1] += len(s) - cnt

        # 2. 길이를 2진법으로 표현한 문자열 생성
        temp = ""
        while cnt > 0:
            temp += str(cnt%2)
            cnt = cnt // 2

        answer[0] += 1
        s = temp[::-1]

    return answer

examples = [
    ["110010101001", [3, 8]],
    ["01110", [3, 3]],
    ["1111111", [4, 1]]
]
for s, r in examples:
    print(solution(s) == r)