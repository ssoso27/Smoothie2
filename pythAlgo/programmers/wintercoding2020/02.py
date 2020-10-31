def solution(encrypted_text, key, rotation):
    answer = ''
    n = len(encrypted_text)

    temp = encrypted_text
    rotation = rotation % n
    if rotation > 0:
        temp = encrypted_text[rotation: ] + encrypted_text[ :rotation]
    elif rotation < 0:
        temp = encrypted_text[n+rotation: ] + encrypted_text[ :n+rotation]

    for idx in range(len(encrypted_text)):
        n = ord(temp[idx]) - ord(key[idx])
        if n < 1:
            n = 26 + n
        if n > 26:
            n = n - 26

        answer += chr(96+n)

    return answer

print(solution("qyyigoptvfb", "abcdefghijk", 3))
print(solution("dabc", "zzzz", -1))
print(solution("bcza", "abcd", -2))
print(solution("aaaa", "aaaa", 2))
print(solution("bac", "dbc", 0))
print(solution("optig", "abcde", -2))
print(solution("igopt", "abcde", 0))
print(solution("yac", "abc", 0))
print(solution("cya", "abc", 1))
print(solution("acy", "abc", -1))
print(solution("cya", "abc", 4))
print(solution("acy", "abc", -4))