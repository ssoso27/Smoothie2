def solution(p,s):
    answer = 0
    for i in range(len(p)):
        pp, ss = map(int, (p[i], s[i]))
        if pp == ss:
            continue
        elif pp < ss:
            if ss - pp <= 5: # 정방향
                answer += ss - pp
            else: # 역방향
                answer += 10 + pp - ss
        elif pp > ss:
            if pp - ss >= 5: # 정방향
                answer += 10 + ss - pp
            else: # 역방향
                answer += pp - ss

    return answer


ex = [
    ("82195", "64723", 13),
    ("00000000000000000000", "91919191919191919191", 20)
]
for p, s, r in ex:
    print(solution(p, s) == r)