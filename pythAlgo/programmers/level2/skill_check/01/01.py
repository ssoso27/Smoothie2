brackets = {
    "(": 1,
    ")": -1
}


def is_correct(u):
    score = 0
    for s in u:
        score += brackets[s]
        if score < 0:
            return False
    return True


def solution(p):
    if len(p) == 0:
        return ""

    score = 0
    for i in range(len(p)):
        score += brackets[p[i]]
        if score == 0: # 제일 작은 균형
            u, v = p[:i+1], p[i+1:]
            if is_correct(u): # 올바른 문자열이면
                return u + solution(v)
            else:
                temp = "(" + solution(v) + ")"
                u = u[1:-1]
                # 방향 뒤집기
                for s in u:
                    if s == "(":
                        temp += ")"
                    elif s == ")":
                        temp += "("
                return temp

ex = {
    "(()())()": "(()())()",
    ")(": "()",
    "()))((()": "()(())()"
}
for p, r in ex.items():
    print(solution(p) == r)