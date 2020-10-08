def solution(new_id):
    answer = ''

    for n in new_id:
        # 1단계
        if 65 <= ord(n) <= 90:
            answer += chr(ord(n)+32)

        # 2단계
        elif 97 <= ord(n) <= 122 \
                or 48 <= ord(n) <= 59 or n == '-' \
                or n == '_':
            answer = answer + n

        # 3단계, 4단계
        elif n == "." :
            if len(answer) > 0 and answer[-1] != ".":
                answer = answer + n

    # 5단계
    if len(answer) == 0:
        answer = "a"
    # 6단계
    elif len(answer) >= 16:
        answer = answer[:15]
        while answer[-1] == ".":
            answer = answer[:-1]
    # 7단계
    elif len(answer) <= 2:
        while len(answer) == 3:
            answer += answer[-1]

    print("최종 : " + new_id + " -> " + answer)
    return answer


examples = [
    ("...!@BaT#*..y.abcdefghijklm", "bat.y.abcdefghi"),
    ("z-+.^.", "z--"),
    ("=.=", "aaa"),
    ("123_.def", "123_.def"),
    ("abcdefghijklmn.p", "abcdefghijklmn")
]
# for n, r in examples:
#     print(solution(n) == r)
print(solution(examples[1][0]) == examples[1][1])