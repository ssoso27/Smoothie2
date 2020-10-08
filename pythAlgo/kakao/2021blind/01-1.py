def solution(new_id):
    answer = ''

    # 1단계
    new_id = str.lower(new_id)

    # 2단계
    for n in new_id:
        if 97 <= ord(n) <= 122 \
                or 48 <= ord(n) <= 59 or n == '-' \
                or n == '_' \
                or n == ".":
            answer += n

    new_id = answer
    answer = ''
    # 3단계
    for i, n in enumerate(new_id):
        if n == "." and new_id[i-1] == ".":
            continue
        answer += n

    # 4단계
    while len(answer) > 0 and (answer[0] == "." or answer[-1] == "."):
        if answer[0] == ".":
            answer = answer[1:]
        elif answer[-1] == ".":
            answer = answer[:-1]

    # 5단계
    if len(answer) == 0:
        answer = "a"
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        while answer[-1] == ".":
            answer = answer[:-1]
    # 7단계
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]

    return answer


examples = [
    ("...!@BaT#*..y.abcdefghijklm", "bat.y.abcdefghi"),
    ("z-+.^.", "z--"),
    ("=.=", "aaa"),
    ("123_.def", "123_.def"),
    ("abcdefghijklmn.p", "abcdefghijklmn")
]
for n, r in examples:
    print(solution(n) == r)
# print(solution(examples[1][0]) == examples[1][1])