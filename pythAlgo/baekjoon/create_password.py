import sys
sys.setrecursionlimit(10**8) # 10^8 까지 늘림.
input = sys.stdin.readline


def is_correct_password(password):
    vowel = 0
    consonant = 0
    for p in password:
        if p in 'aeiou':
            vowel += 1
        else:
            consonant += 1

    if vowel >= 1 and consonant >= 2:
        return True
    return False


def backtracking(idx, password):
    # password 가 다 채워졌을 때
    if idx == L:
        # 조건 검사
        if is_correct_password(password):
            print("".join(password))
            return

    for i in range(len(characters)):
        # 이미 들어가있는 글자면
        if checked[i]:
            continue

        # 오름차순 정렬이 아니면
        if idx > 0 and ord(password[-1]) > ord(characters[i]):
            continue

        # 패스워드에 추가하고
        password += characters[i]
        checked[i] = True

        # 백트래킹
        backtracking(idx+1, password)

        # 돌아오면 다시 돌려놈
        checked[i] = False
        password = password[:-1]


L, C = map(int, input().split(" "))
characters = sorted(list(map(str, input().strip().split(" "))))

checked = [False] * C

backtracking(0, '')
