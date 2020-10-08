import re


check = set()
def backtracking(idx, possible_id, johab):
    global check
    # 조건에 맞는 조합이 이루어짐
    if idx == len(possible_id):
        check.add(" ".join(sorted(johab)))
        return

    for id in possible_id[idx]:
        # 이미 들어있다면
        if id in johab:
            continue

        johab.append(id)
        backtracking(idx+1, possible_id, johab)

        johab.pop()


def solution(user_id, banned_id):

    for i in range(len(banned_id)):
        new_banned = ""
        for j in range(len(banned_id[i])):
            if banned_id[i][j] == "*":
                new_banned += "."
            else:
                new_banned += banned_id[i][j]
        banned_id[i] = new_banned

    possible_id = [[] for _ in range(len(banned_id))]
    for i in range(len(banned_id)):
        banned = banned_id[i]
        p = re.compile(banned)
        for j in range(len(user_id)):
            user = user_id[j]
            if len(user) != len(banned):
                continue

            m = p.match(user)
            if m:
                possible_id[i].append(user)

        # # 똑같은 아이디 후보가 있는지 확인
        # if possible_id[i] in possible_id[:i]:
        #     possible_id.pop()

    johab = []
    backtracking(0, possible_id, johab)

    return len(check)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
print(solution(user_id, banned_id))